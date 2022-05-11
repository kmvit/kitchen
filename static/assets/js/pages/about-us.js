jQuery(function($) {
    "use strict";

    var SLZ = window.SLZ || {};


    /*=======================================
    =        SLIDE VERTICAL FUNCTION        =
    =======================================*/

    SLZ.slideVertical = function() {

        setTimeout(function() {

            // Slide gallery widget
            $('.slide-gallery').slick({
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
            var height_client_slick_dots = ($('.client-slick-2 .slick-dots').height() / 2) - 40;
            $('.client-slick-2 .slick-dots').css('margin-top', '-' + height_client_slick_dots + 'px');

            // Set position banner image why us
            var box_img_width = $('.why-us.layout-1 .box-img img').width() / 2;
            $('.why-us.layout-1 .box-img').css('left', '-' + (box_img_width - 10) + 'px');

            // Slide client widget
            $('.client-slick-2').slick({
                infinite: true,
                slidesToShow: 1,
                slidesToScroll: 1,
                speed: 1000,
                arrows: false,
                dots: true,
                vertical: true,
                autoplay: true,
                appendArrows: $('.nav-slide-client2'),
                appendDots: $('.nav-slide-client2'),
                customPaging: function(slider, i) {
                    return '<a>' + i + '</a>';
                },
            });

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
