jQuery(document).ready(($) => {
    if ($(window).width() < 576) {

        // text your vars
        let titleBlock = $('.title-wrapper'),
            content = $('.section-content');
        ////////////////

        $(content).hide();

        function colorTitleBlock() {
            let titles = $(titleBlock).find('h2').prev('.sub-title');
            $(titles).each((i, item) => {
                let color = $(item).css('background')
                $(titleBlock).eq(i).css('background', color).css('padding', '30px 10px');
            });
        }

        colorTitleBlock();

        $(titleBlock).each((i, item) => {
            $(item).on('click', () => {
                if ($(item).hasClass('shown')) {
                    $(item).removeClass('shown')
                    $(content).eq(i).slideUp().css('visibility', 'hidden')
                } else {
                    $(item).addClass('shown')
                    $(content).eq(i).slideDown().css('visibility', 'visible')
                }
            });
        });
    }
});