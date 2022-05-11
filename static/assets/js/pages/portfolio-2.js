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
            var $grid = $('.gallery-masonry-isotope').isotope({
                itemSelector: '.content-grid-item',
                layoutMode: 'masonry',
                percentPosition: true,
                masonry: {
                    columnWidth: '.grid-sizer',
                }
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
    });

    /*=====  End of INIT FUNCTIONS  ======*/



});
