const stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
const clientSecret = $('#id_client_secret').text().slice(1, -1);
const errorDiv = $("#error-message");

const stripe = stripe(stripePublicKey);

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

let card = elements.create('card', {'style':style})
card.mount('#payment-element');

//validation errors on card payment
let getErrorMessage=(event)=>{
    return `
    <span role="alert">
    <i class="fa-solid fa-triangle-exclamation fa-sm"></i>
    </span>
    <span>${event.error.message}</span>
    `;

}

card.on('change', (event) => {
    if (event.error) {
        let errorText = getErrorMessage(event);
        $(errorDiv).html(errorText);
    } else {
        $(errorDiv).text(''); // Clear the error message when input is valid
    }
});

// Handle form submision

const form = document.getElementById('payment-form');

form.addEventListener('submit', function(event) {
    event.preventDefault();
    card.update({'disabled': true});
    $('#submit-button').attr({'disabled':true});

    let saveInfo = Boolean($('#id-save-info').attr('checked'));
    let csrfToken  = $('input[name="csrfmiddlewaretoken"]').val();
    let postData = {

    };

    const url = '/checkout/cache_checkout_data/'
    $.post(url, postData).done(function)(){
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details:{
                    billing_details: {
                        name: $.trim(paymentForm.full_name.value),
                        phone: $.trim(paymentForm.phone_number.value),
                        email: $.trim(paymentForm.email.value),
                        address: {
                            line1: $.trim(paymentForm.street_address1.value),
                            line2: $.trim(paymentForm.street_address2.value),
                            city: $.trim(paymentForm.town_or_city.value),
                            country: $.trim(paymentForm.country.value),
                            state: $.trim(paymentForm.county.value),
                        }
                    }
                },
                shipping: {
                    name: $.trim(paymentForm.full_name.value),
                    phone: $.trim(paymentForm.phone_number.value),
                    address: {
                        line1: $.trim(paymentForm.street_address1.value),
                        line2: $.trim(paymentForm.street_address2.value),
                        city: $.trim(paymentForm.town_or_city.value),
                        country: $.trim(paymentForm.country.value),
                        postal_code: $.trim(paymentForm.postcode.value),
                        state: $.trim(paymentForm.county.value),
                    }
                }                    
                }
            
        }).then(function(result) {
            if (result.error) {
                let errorText=getErrorMessage(result)
                $(errorDiv).html(errorText);
                card.update({'disabled': false})
                $('#submit-button').attr({'disabled':false})
          } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        }).fail(function(){
            location.reload();
        })
}
});



