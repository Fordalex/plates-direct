$(document).ready(function() {
    $('.mobile-links-container li').css('transform', 'translateX(-70vw)');
});

$(document).on('click', '.burger-container', function() {
   toggleNavigation();
})

$(document).on('click', '.page-content', function() {
    toggleNavigation();
})

$(document).on('click', '.menu-overlay', function() {
    toggleNavigation();
})

function toggleNavigation() {
    $('.mobile-links-container').css('display', 'block');
    if ($('.mobile-links-container').hasClass('open')) {
        // close the navigation animation
        anime({
            targets: '.mobile-links-container li',
            translateX: '-70vw',
            duration: 0,
            easing: 'easeInOutQuad',
          });
        anime({
            targets: '.mobile-links-container',
            translateX: -50,
            duration: 200,
            easing: 'easeInOutQuad',
          });
          anime({
            targets: '.burger-mid',
            opacity: '1',
        });
        anime({
            targets: '.burger-top',
            rotateZ: '0deg',
            translateY : '0',
        })
        anime({
            targets: '.burger-bottom',
            rotateZ: '0deg',
            translateY: '0'
        })
        $('.menu-overlay').css('display', 'none');
    } else {
        // open the navigation animation
        $('.menu-overlay').css('display', 'block');
        anime({
            targets: '.mobile-links-container',
            translateX: '65vw',
            duration: 200,
            easing: 'easeInOutQuad',
          });
        anime({
            targets: '.mobile-links-container li',
            translateX: '0vw',
            duration: 200,
            easing: 'easeInOutQuad',
            delay: anime.stagger(100, {start: 100}),
          });
        anime({
            targets: '.burger-mid',
            opacity: '0',
        });
        anime({
            targets: '.burger-top',
            rotateZ: '45deg',
            translateY: '12px',
        })
        anime({
            targets: '.burger-bottom',
            rotateZ: '-45deg',
            translateY: '-12px',
        })
    }
    $('.mobile-links-container').toggleClass('open');
}