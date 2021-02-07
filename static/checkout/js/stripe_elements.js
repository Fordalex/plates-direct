var stripePublicKey = $('#id_stripe_public_key').text().slice(1,-1);
var clientSecret = $('#id_client_secret').text().slice(1,-1);
var stripe = Stripe(stripePublicKey)
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

// Handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
  var errorDiv = document.getElementById('card-errors');
  if (event.error) {
      var html = `
          <span class="icon" role="alert">
              <i class="fas fa-times"></i>
          </span>
          <span>${event.error.message}</span>
      `;
      $(errorDiv).html(html);
  } else {
      errorDiv.textContent = '';
  }
});

// Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
  ev.preventDefault();
  card.update({ 'disabled': true});
  $('#submit-button').attr('disabled', true);
  stripe.confirmCardPayment(clientSecret, {
      payment_method: {
          card: card,
      }
  }).then(function(result) {
      if (result.error) {
          var errorDiv = document.getElementById('card-errors');
          var html = `
              <span class="icon" role="alert">
              <i class="fas fa-times"></i>
              </span>
              <span>${result.error.message}</span>`;
          $(errorDiv).html(html);
          card.update({ 'disabled': false});
          $('#submit-button').attr('disabled', false);
      } else {
          if (result.paymentIntent.status === 'succeeded') {
              console.log('payment successful')
              form.submit();
          }
      }
  });
});

function sendEmail() {
  var data = {
    service_id: 'gmail',
    template_id: 'plates_direct',
    user_id: 'user_fFFNDDJRdm6W6POwiDzok',
    template_params: {
        'full_name': 'test',
        'email': 'test',
        'subject': 'test',
        'information': 'test',
    }
};
$.ajax('https://api.emailjs.com/api/v1.0/email/send', {
    type: 'POST',
    data: JSON.stringify(data),
    contentType: 'application/json'
}).done(function () {
    $('#form_container').html(`
                    <div class="col-12 d-flex justify-content-center">
                        <p class="text-center text-success mt-4">Your message has been sent!</p>
                    </div>`)
}).fail(function (error) {
    alert('Oops... ' + JSON.stringify(error) + 'Your order has been placed but there has been a problem with your confirmation email. Please send us an email to: plates-direct@hotmail.com. your order number is xxxxxxxx');
});
}


