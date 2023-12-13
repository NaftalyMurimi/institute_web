$(document).ready(function(){
    $('.counter-value').each(function(){
        $(this).prop('Counter',0).animate({
            Counter: $(this).text()
        },{
            duration: 2000,
            easing: 'easeInQuad',
            step: function (now){
                $(this).text(Math.ceil(now));
            }
        });
    });
});