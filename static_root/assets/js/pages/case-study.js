jQuery(function($) {
    "use strict";

    var SLZ = window.SLZ || {};


    /*=======================================
    =        SLIDE VERTICAL FUNCTION        =
    =======================================*/

    SLZ.slideVertical = function() {
        setTimeout(function() {
            // Slide gallery widget
            $('.about-project .slide-gallery').slick({
                infinite: true,
                slidesToShow: 1,
                slidesToScroll: 1,
                speed: 1000,
                arrows: true,
                dots: true,
                vertical: true,
                appendArrows: $('.nav-slide-gallery'),
                appendDots: $('.nav-slide-gallery'),
                customPaging: function(slider, i) {
                    return '<a>' + i + '</a>';
                },
            });

            // Set slick dots vertical middle
            var height_slick_dots = ($('.slide-gallery .slick-dots').height() / 2);
            $('.slide-gallery .slick-dots').css('margin-top', '-' + height_slick_dots + 'px');

        }, 800);

    };

    /*=====  End of SLIDE VERTICAL FUNCTION  ======*/




    /*======================================
    =            INIT FUNCTIONS            =
    ======================================*/

    $(document).ready(function() {
        SLZ.slideVertical();
    });

    /*=====  End of INIT FUNCTIONS  ======*/


});
