jQuery(function($) {
    "use strict";

    var SLZ = window.SLZ || {};


    /*=======================================
     =        SLIDE VERTICAL FUNCTION        =
     =======================================*/

    SLZ.slideVertical = function() {

        // show gallery
        $(".fancybox").fancybox({
            prevEffect  : 'none',
            nextEffect  : 'none',
            helpers : {
                title   : {
                    type: 'outside'
                },
                thumbs  : {
                    width   : 60,
                    height  : 60
                }
            }
        });

        $(window).on('load', function() {
            // Isotope portfolio filter
            var $grid = $('.gallery-portfolio').isotope({
                itemSelector: '.grid-box-item',
                layoutMode: 'masonry',
                percentPosition: true,
                gutter: 30
            });
            $('.filter-button-group').on('click', 'a', function() {
                $('.filter-button-group > a').removeClass('active');
                $(this).addClass('active');
                var filterValue = $(this).attr('data-filter');
                $grid.isotope({ filter: filterValue });
            });
        });

    };

    /*=====  End of SLIDE VERTICAL FUNCTION  ======*/


    /*======================================
     =            INIT FUNCTIONS            =
     ======================================*/

    $(document).ready(function() {
        SLZ.slideVertical();

        /* Count size padding image */

        // var value = $(window).width() * (15 / 1920);
        // var valuePositive = value + "px";
        // var valueNegative = -value + "px";

        // Change margin
        // $(".margin-portfolio").css({
        //     "margin-left": valueNegative,
        //     "margin-right": valueNegative
        // });

        // $(".pic").css({
        //     "margin": valuePositive
        // });

        // $(".pic-2").css({
        //     "margin": valuePositive
        // });

        // // For Portfolio-Homepage-Advertising: Waring (*)
        // /* Count size padding image */
        // var value2 = $(window).width() * (5 / 1920);
        // var valuePositive2 = value2 + "px";
        // var valueNegative2 = -value2 + "px";

        // // Change margin
        // $(".margin-portfolio-2").css({
        //     "margin-left": valueNegative2,
        //     "margin-right": valueNegative2
        // });


        // $(".pic").css({
        //     "margin": valuePositive2
        // });

        // $(".pic-2").css({
        //     "margin": valuePositive2
        // });

        /*
        var value = $(window).width() * (15 / 1920);
        var valuePositive = value + "px";
        var valueNegative = -value + "px";

        // Change margin
        $(".margin-portfolio").css({
            "margin-left": valueNegative,
            "margin-right": valueNegative
        });

        $(".pic").css({
            "margin": valuePositive
        });

        $(".pic-2").css({
            "margin": valuePositive
        });

        // For Portfolio-Homepage-Advertising: Waring (*)
        /* Count size padding image */
        /*
        var value2 = $(window).width() * (5 / 1920);
        var valuePositive2 = value2 + "px";
        var valueNegative2 = -value2 + "px";

        // Change margin
        $(".margin-portfolio-2").css({
            "margin-left": valueNegative2,
            "margin-right": valueNegative2
        });


        $(".margin-portfolio-2 .pic").css({
            "margin": valuePositive2
        });

        $(".margin-portfolio-2 .pic-2").css({
            "margin": valuePositive2
        });*/
    });

    $( window ).bind("resize", function(){
        // For Portfolio-05
        /* Count size padding image */
        // var value = $(window).width() * (15 / 1920);
        // var valuePositive = value + "px";
        // var valueNegative = -value + "px";
        /*
        var value = $(window).width() * (15 / 1920);
        var valuePositive = value + "px";
        var valueNegative = -value + "px";

        // // Change margin
        // $(".margin-portfolio").css({
        //     "margin-left": valueNegative,
        //     "margin-right": valueNegative
        // });


        // $(".pic").css({
        //     "margin": valuePositive
        // });

        // $(".pic-2").css({
        //     "margin": valuePositive
        // });

        // // For Portfolio-Homepage-Advertising: Waring (*)
        // /* Count size padding image */
        // var value2 = $(window).width() * (5 / 1920);
        // var valuePositive2 = value2 + "px";
        // var valueNegative2 = -value2 + "px";

        // For Portfolio-Homepage-Advertising: Waring (*)
        /* Count size padding image */
        /*
        var value2 = $(window).width() * (5 / 1920);
        var valuePositive2 = value2 + "px";
        var valueNegative2 = -value2 + "px";


        // // Change margin
        // $(".margin-portfolio-2").css({
        //     "margin-left": valueNegative2,
        //     "margin-right": valueNegative2
        // });



        // $(".pic").css({
        //     "margin": valuePositive2
        // });

        // $(".pic-2").css({
        //     "margin": valuePositive2
        // });

        $(".margin-portfolio-2 .pic").css({
            "margin": valuePositive2
        });

        $(".margin-portfolio-2 .pic-2").css({
            "margin": valuePositive2
        });*/

    });

    /*=====  End of INIT FUNCTIONS  ======*/


});
