import Swiper from 'https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.mjs'

const swiper = new Swiper('.swiper', {
    direction: 'horizontal',
    loop: true,

    pagination: {
        el: '.swiper-pagination',
    },
    effect: 'fade',
    fadeEffect: {
        crossFade: true,
    },
    autoplay: {
        delay: 3000,
    },
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },

    scrollbar: {
        el: '.swiper-scrollbar',
    },
});

const burgerMenu = document.getElementById('menu');
const burgerToggle = document.getElementById('menuCheckbox');

// Close menu when clicking outside
document.addEventListener('click', function (event) {
    const isClickInsideMenu = burgerMenu.contains(event.target);
    const isClickOnToggle = document.getElementById('menuToggle').contains(event.target);

    if (!isClickInsideMenu && !isClickOnToggle) {
        burgerToggle.checked = false; // uncheck checkbox to close menu
    }
});