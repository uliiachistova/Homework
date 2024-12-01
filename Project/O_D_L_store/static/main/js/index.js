document.addEventListener('DOMContentLoaded', function () {
    const swiper = new Swiper('.swiper-container', {
        loop: true,
        autoplay: {
            delay: 10000,
            disableOnInteraction: true,
        },
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
            dynamicBullets: true,
        },
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
        slidesPerView: 1,
        effect: 'fade',
        fadeEffect: {
            crossFade: true
        },
    });
});


function toggleFilter(filterId) {
    const filter = document.getElementById(filterId);
    filter.classList.toggle('hidden');
}

function applyFilters() {
    const colors = Array.from(document.querySelectorAll('input[name="color"]:checked')).map(input => input.value);
    const shapes = Array.from(document.querySelectorAll('input[name="shape"]:checked')).map(input => input.value);
    const search = document.getElementById('search-box').value;
    const sort = document.getElementById('sort-options').value;
    console.log('Фильтры:', { colors, shapes, search, sort });

    const results = document.getElementById('catalog-results');
}
