$(document).on('keyup','#view-plates', function() {
    var numberPlate = $('#view-plates').val();
    $('#yellow-number-plate').html(numberPlate);
    $('#white-number-plate').html(numberPlate);
    if (!checkoutButton) {
        $('#checkout-button-container').html('<button class="btn btn-info container-fluid mt-2">Checkout</button>')
    }
});

var checkoutButton = false;





