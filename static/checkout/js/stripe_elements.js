var stripe_public_key = $('#id_stripe_public_key').text().slice(1,-1);
var client_secret = $('#id_client_secret').text().slice(1,-1);
var stripe = Stripe(stripe_public_key)

var elements = stripe.elements();
var card = elements.create('card');

var style = {
    base: {
      color: "#32325d",
      fontFamily: 'Arial, sans-serif',
      fontSmoothing: "antialiased",
      fontSize: "16px",
      "::placeholder": {
        color: "#32325d"
      }
    },
    invalid: {
      fontFamily: 'Arial, sans-serif',
      color: "#fa755a",
      iconColor: "#fa755a"
    }
  };

card.mount('#card-element', {style: style});



