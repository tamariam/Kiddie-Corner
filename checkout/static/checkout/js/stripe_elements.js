const stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
const client_secret = $('#id_client_secret').text().slice(1, -1);
const errorDiv = $("#error-message");

const stripe = Stripe(stripe_public_key);

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

card.on('change', (event)=>{
    if (event.error){
    let errorText=getErrorMessage(event)
    $(errorDiv).html(errorText);
    }else {
        errorDiv.textContent = '';
    }
})



