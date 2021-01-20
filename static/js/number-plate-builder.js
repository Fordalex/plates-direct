$(document).on('keyup','#view-plates', function() {
    var numberPlate = $('#view-plates').val();
    $('#yellow-number-plate').html(numberPlate);
    $('#white-number-plate').html(numberPlate);
});





