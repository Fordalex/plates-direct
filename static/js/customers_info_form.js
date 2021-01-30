$('#send_email').on('click', function() {
    console.log($('#full_name').val())
    if ($('#full_name').val() == '') {
        $('#error').html('<p class="text-danger">Please enter your name.</p>')
    } else if ($('#email').val() == '') {
        $('#error').html('<p class="text-danger">Please enter an email address.</p>')
    } else if ($('#subject').val() == '') {
        $('#error').html('<p class="text-danger">Please select an option.</p>')
    } else if ($('#information').val() == '') {
        $('#error').html('<p class="text-danger">Please enter some information.</p>')
    } else {
        var data = {
            service_id: 'gmail',
            template_id: 'lavish',
            user_id: 'user_fFFNDDJRdm6W6POwiDzok',
            template_params: {
                'full_name': $('#full_name').val(),
                'email': $('#email').val(),
                'subject': $('#subject').val(),
                'information': $('#information').val(),
            }
        };
        $.ajax('https://api.emailjs.com/api/v1.0/email/send', {
            type: 'POST',
            data: JSON.stringify(data),
            contentType: 'application/json'
        }).done(function() {
            $('#form_container').html(`
                    <div class="col-12 d-flex justify-content-center">
                        <p class="text-center text-success mt-4">Your message has been sent!</p>
                    </div>`)
        }).fail(function(error) {
            alert('Oops... ' + JSON.stringify(error));
        });
    }
});