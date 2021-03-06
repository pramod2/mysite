// Shorthand for $( document ).ready()
$(function() {
    //google analytics
    googleAnalytics(window, document, 'script', 'https://www.google-analytics.com/analytics.js', 'ga');
    ga('create', 'UA-79396007-1', 'auto');
    ga('send', 'pageview');

    //totalShares
    totalShares();
});


function googleAnalytics(i, s, o, g, r, a, m) {
    i['GoogleAnalyticsObject'] = r;
    i[r] = i[r] || function() {
        (i[r].q = i[r].q || []).push(arguments)
    }, i[r].l = 1 * new Date();
    a = s.createElement(o),
        m = s.getElementsByTagName(o)[0];
    a.async = 1;
    a.src = g;
    m.parentNode.insertBefore(a, m)
}

function totalShares() {
  var dr = document.createElement('script');
  dr.type = 'text/javascript'; dr.async = true;
  dr.src = '//share.donreach.com/buttons.js';
  (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dr);
}


/*
// Navigation Scripts to Show social shares on Scroll-Up
jQuery(document).ready(function($) {
    var MQL = 1170;

    //primary navigation slide-in effect
    if ($(window).width() > MQL) {
        var headerHeight = $('.social-buttons').height();
        $(window).on('scroll', {
                previousTop: 0
            },
            function() {
                var currentTop = $(window).scrollTop();
                //check if user is scrolling up
                if (currentTop < this.previousTop) {
                    //if scrolling up...
                    if (currentTop > 0 && $('.social-buttons').hasClass('is-fixed')) {
                        $('.social-buttons').addClass('is-visible');
                    } else {
                        $('.social-buttons').removeClass('is-visible is-fixed');
                    }
                } else {
                    //if scrolling down...
                    $('.social-buttons').removeClass('is-visible');
                    if (currentTop > headerHeight && !$('.social-buttons').hasClass('is-fixed')) $('.social-buttons').addClass('is-fixed');
                }
                this.previousTop = currentTop;
            });
    }
});
*/