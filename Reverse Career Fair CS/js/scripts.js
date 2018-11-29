// scrolling
// if (window.addEventListener) window.addEventListener('DOMMouseScroll', wheel, false);
// window.onmousewheel = document.onmousewheel = wheel;

// function wheel(event) {
//     var delta = 0;
//     if (event.wheelDelta) delta = event.wheelDelta / 120;
//     else if (event.detail) delta = -event.detail / 3;

//     handle(delta);
//     if (event.preventDefault) event.preventDefault();
//     event.returnValue = false;
// }

// function handle(delta) {
//     var time = 250;
//     var distance = 250;

//     $('html, body').stop().animate({
//         scrollTop: $(window).scrollTop() - (distance * delta)
//     }, time );
// }

/*back to top button*/
$(document).ready(function() {
    var offset=600, // At what pixels show Back to Top Button
    scrollDuration=300; // Duration of scrolling to top

    $(window).scroll(function() {
        if ($(this).scrollTop() > offset) {
            $('.top').fadeIn(500); // Time(in Milliseconds) of appearing of the Button when scrolling down.    
        } else {
            $('.top').fadeOut(400); // Time(in Milliseconds) of disappearing of Button when scrolling up.
        }
    });


    // Smooth animation when scrolling
    $('.top').click(function(event) {
        event.preventDefault();
        $('html, body').animate({scrollTop: 0}, scrollDuration);
    });

    // Size bg image on load
    $('.background img').each(function() {
        console.log("run");
        var maxWidth = $(window).width(); // Max width for the image
        var maxHeight = 600;    // Max height for the image
        var ratio = 2;  // Used for aspect ratio
        var width = $(this).width();    // Current image width 1225
        var height = $(this).height();  // Current image height

        // Check if the current width is larger than the max
        if(width > maxWidth){
            $(this).css("min-height", "100%");
            $(this).css("min-width", 0);
        } else {
            $(this).css("min-width", "100%");
            $(this).css("min-height", 0);
        }
    });
});

$(window).resize(function() {
    $('.background img').each(function() {
        var maxWidth = $(window).width(); // Max width for the image
        var maxHeight = 600;    // Max height for the image
        var ratio = 2;  // Used for aspect ratio
        var width = $(this).width();    // Current image width 1225
        var height = $(this).height();  // Current image height

        // Check if the current width is larger than the max
        if(width > maxWidth){
            $(this).css("min-height", "100%");
            $(this).css("min-width", 0);
        } else {
            $(this).css("min-width", "100%");
            $(this).css("min-height", 0);
        }
    });
});

$(document).ready(function(){
    $("html").delay(200).fadeIn(750)
});


