$('.input-number').keyup(function() {
    var num = $(this)
    number = num.val() - parseFloat( num.val() ) >= 0
    if(number !== true){
    	num.val(" ")
    }
    if(num.val() == ""){
        num.val(" ")
    }
});


