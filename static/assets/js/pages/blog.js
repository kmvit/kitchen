$(function() {
  "use strict";

    $.fn.datepicker.dates['en'] = {
      days: ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
      daysShort: ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"],
      daysMin: ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"],
      months: ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
      monthsShort: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
      today: "Today",
      clear: "Clear",
      format: "mm/dd/yyyy",
      titleFormat: "MM yyyy", /* Leverages same syntax as 'format' */
      weekStart: 0
    };
    
    $('#datetimepickerWiget').datepicker({
      todayHighlight: true,
      beforeShowDay: function(e) {
        if ($('.datepicker-days .datepicker-switch').length) {
          var switchHTML = $('.datepicker-days .datepicker-switch');
          var titleDate = switchHTML.text();
          var titleDateArr = titleDate.split(' ');
          var titleMonth = titleDateArr[0];
          titleMonth = '<span class="month-base">'+titleMonth+'</span>';
          switchHTML.html(titleMonth+' '+titleDateArr[1]);
        }
        
        
      }
    });
      
  /* Audio post */
  if($('#player2').length > 0) {
    $('#player2').mediaelementplayer({
      audioWidth: '100%',
      audioHeight: 60
    });
  }

  if($(".video-embed").length) {
        var gurl = $(".video-embed")[0].src;
        var height_video = $('.video-button-play').parents('.post-image').height();

        $(window).resize(function() {

            height_video = $('.video-button-play').parents('.post-image').height();
        });
        $(".video-button-play").on('click', function(event) {
            $('.video-bg, .video-button-play').addClass('fadeOut hide-video').removeClass('fadeIn show-video');
            $(".video-embed, .video-button-close").addClass('fadeIn show-video').removeClass('fadeOut hide-video');
            $(".video-embed")[0].src += "&autoplay=1";
            event.preventDefault();
        });

        $(".video-button-close").on('click', function(event) {
            $(".video-embed")[0].src = gurl;
            $('.video-bg, .video-button-play').addClass('fadeIn show-video').removeClass('fadeOut hide-video');
            $(".video-embed, .video-button-close").addClass('fadeOut hide-video').removeClass('fadeIn show-video');
            $('.video-button-close').removeClass('show-video');

        });
    }

    if($('.blog-base').length && $(window).width() > 480) {
      setTimeout(function() {
        $('.blog-base').isotope({
            itemSelector: '.item-base',
            layoutMode: 'masonry',
            percentPosition: true
        });
      },300);
    }

    // console.log($('.datepicker-switch').text());

});