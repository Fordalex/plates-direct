$('#addPersonalInformation').submit(function(e){
    e.preventDefault();
    $('#errorContainer').html(" ");
    let nextPage = true;

    // general
    if (!$('#firstName').val()) {
        nextPage = false;
        $('#errorContainer').append('<p class="text-danger m-0">Please enter your first name.</p>')
    }
    if (!$('#lastName').val()) {
        nextPage = false;
        $('#errorContainer').append('<p class="text-danger m-0">Please enter your last name.</p>')
    }
    if (!$('#email').val()) {
        nextPage = false;
        $('#errorContainer').append('<p class="text-danger m-0">Please enter your email.</p>')
    }
    if (!$('#phoneNumber').val()) {
        nextPage = false;
        $('#errorContainer').append('<p class="text-danger m-0">Please enter your phone number.</p>')
    }

    // address
    if (!$('#firstLineAdress').val()) {
        nextPage = false;
        $('#errorContainer').append('<p class="text-danger m-0">Please enter your first name.</p>')
    }
    if (!$('#townOrCity').val()) {
        nextPage = false;
        $('#errorContainer').append('<p class="text-danger m-0">Please enter your last name.</p>')
    }
    if (!$('#county').val()) {
        nextPage = false;
        $('#errorContainer').append('<p class="text-danger m-0">Please enter your email.</p>')
    }
    if (!$('#postcode').val()) {
        nextPage = false;
        $('#errorContainer').append('<p class="text-danger m-0">Please enter your phone number.</p>')
    }

    if (nextPage) {
        $('#addPersonalInformation')[0].submit();
    }

});



console.log('page connected')