$(document).on('keyup','#reg_number', function() {
    numberPlate = $('#reg_number').val();
    updatePlates()
});

var numberPlate = 'PL35 DCT';
var viewPlates = 'both';


function updatePlates() {
    var frontPlate = `
            <div id="viewBackPlate" class="number-plate-container number-plate-container-white ">
                <p class="number-plate-font" id="yellow-number-plate">${numberPlate}</p>
            </div>
    `;

    var backPlate = `
                <div id="viewFrontPlate" class="number-plate-container number-plate-container-yellow mb-2">
                    <p class="number-plate-font" id="white-number-plate">${numberPlate}</p>
                </div>
    `;

    if (viewPlates == 'both') {
        $('#plateContainer').html(backPlate);
        $('#plateContainer').append(frontPlate);
        $('.price').html('£19.99');
    } else if (viewPlates == 'front') {
        $('#plateContainer').html(frontPlate);
        $('.price').html('£10.99');
    } else {
        $('#plateContainer').html(backPlate);
        $('.price').html('£10.99');
    }

}

$(document).on('click', '#frontPlateButton', function() {
    viewPlates = 'front';
    $('#item').val('front');
    updatePlates()
});

$(document).on('click', '#backPlateButton', function() {
    viewPlates = 'back';
    $('#item').val('back');
    updatePlates()
});

$(document).on('click', '#bothPlateButton', function() {
    viewPlates = 'both';
    $('#item').val('both');
    updatePlates()
});

// Change the style of the button thats been selected.
$(document).on('click', '.toggle-plate-button', function() {
    $('#frontPlateButton').removeClass('bg-main')
    $('#backPlateButton').removeClass('bg-main')
    $('#bothPlateButton').removeClass('bg-main')

    $('#'.concat(this.id)).addClass('bg-main')

})