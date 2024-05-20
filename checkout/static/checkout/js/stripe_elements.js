$(document).ready(function() {
    const stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
    const clientSecret = $('#id_client_secret').text().slice(1, -1);
    const errorDiv = $("#error-message");

    // Ensure stripePublicKey is valid
    if (!stripePublicKey) {
        console.error('Stripe public key not found');
        return;
    }

    const stripe = Stripe(stripePublicKey);

    let elements = stripe.elements();
    let style = {
        base: {
            color: '#000',
            fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
            fontSmoothing: 'antialiased',
            fontSize: '19px',
            '::placeholder': {
                color: '#aab7c4'
            }
        },
        invalid: {
            color: '#dc3545',
            iconColor: '#dc3545'
        }
    };

    let card = elements.create('card', { 'style': style });

    // Ensure #payment-element exists
    if ($('#payment-element').length) {
        card.mount('#payment-element');
    } else {
        console.error('#payment-element not found');
        return;
    }

    // Validation errors on card payment
    let getErrorMessage = (event) => {
        return `
        <span role="alert">
        <i class="fa-solid fa-triangle-exclamation fa-sm"></i>
        </span>
        <span>${event.error.message}</span>
        `;
    };

    card.on('change', (event) => {
        if (event.error) {
            let errorText = getErrorMessage(event);
            $(errorDiv).html(errorText);
        } else {
            $(errorDiv).text(''); // Clear the error message when input is valid
        }
    });

    // Handle form submission
    const form = document.getElementById('payment-form');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        card.update({ 'disabled': true });
        $('#submit-button').attr({ 'disabled': true });
        let saveInfo = Boolean($('#id-save-info').attr('checked'));
        // From using {% csrf_token %} in the form
        let csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
        let postData = {
            'csrfmiddlewaretoken': csrfToken,
            'client_secret': clientSecret,
            'save_info': saveInfo,
        };
        const url = '/checkout/cache_checkout_data/';
        $.post(url, postData).done(function() {
            stripe.confirmCardPayment(clientSecret, {
                payment_method: {
                    card: card,
                    billing_details: {
                        name: $.trim(form.full_name.value),
                        phone: $.trim(form.phone_number.value),
                        email: $.trim(form.email.value),
                        address: {
                            line1: $.trim(form.street_address1.value),
                            line2: $.trim(form.street_address2.value),
                            city: $.trim(form.town_or_city.value),
                            country: $.trim(form.country.value),
                            state: $.trim(form.county.value),
                        }
                    }
                },
                shipping: {
                    name: $.trim(form.full_name.value),
                    phone: $.trim(form.phone_number.value),
                    address: {
                        line1: $.trim(form.street_address1.value),
                        line2: $.trim(form.street_address2.value),
                        city: $.trim(form.town_or_city.value),
                        country: $.trim(form.country.value),
                        postal_code: $.trim(form.postcode.value),
                        state: $.trim(form.county.value),
                    }
                }
            }).then(function(result) {
                if (result.error) {
                    let errorText = getErrorMessage(result);
                    $(errorDiv).html(errorText);
                    card.update({ 'disabled': false });
                    $('#submit-button').attr({ 'disabled': false });
                } else {
                    if (result.paymentIntent.status === 'succeeded') {
                        form.submit();
                    }
                }
            });
        }).fail(() => {
            // Just reload the page, the error will be in Django messages
            location.reload();
        });
    });
});