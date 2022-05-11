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

            setTimeout(function() {
                var $grid = $('.gallery .gallery-masonry').isotope({
                    itemSelector: '.block-item-wrapper',
                    layoutMode: 'masonry',
                    percentPosition: true,
                    masonry: {
                       columnWidth: '.grid-sizer'
                       // gutter: 5
                   }
                });
                var $grid1 = $('.gallery-case-study .gallery-masonry');
                    $grid1.isotope({
                    itemSelector: '.block-item-wrapper',
                    layoutMode: 'fitRows',
                    percentPosition: true,
                    masonry: {
                       columnWidth: '.grid-sizer'
                   }
                });
                var $grid2 = $('.gallery-portfolio').isotope({
                    itemSelector: '.grid-box-item',
                    layoutMode: 'masonry',
                    percentPosition: true,
                    masonry: {
                        columnWidth: '.grid-sizer'
                        // gutter: 5
                    }
                });
                $('.filter-button-group').on('click', 'a', function() {
                    $('.filter-button-group > a').removeClass('active');
                    $(this).addClass('active');
                    var filterValue = $(this).attr('data-filter');
                    $grid.isotope({ filter: filterValue });
                    $grid1.isotope({ filter: filterValue });
                    $grid2.isotope({ filter: filterValue });
                });
            }, 300);
            
            $(".gallery-masonry .block-item-wrapper a").fancybox({
                helpers : {
                    thumbs  : {
                        width   : 60,
                        height  : 60
                    }
                }
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
