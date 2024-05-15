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
    card.update({'disabled': true})
    $('#submit-button').attr({'disabled':true})
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
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
    });
});



