new WOW().init()

const swiperSport = new Swiper('.swiper-container-sport', {
    loop: true,
    effect: 'coverflow',
    grabCursor: true,
    centeredSlides: true,
    slidesPerView: 'auto',
    coverflowEffect: {
        rotate: 50,
        stretch: 0,
        depth: 100,
        modifier: 1,
        slideShadows: true,
    },
    pagination: {
        el: '.sport-pagination',
        bulletClass: "sport-bullet",
        bulletActiveClass: "sport-bullet-active",
        clickable: true,
    },
});

const swiper = new Swiper('.swiper-container-sight', {
    slidesPerView: 2,
    slidesPerColumn: 2,
    slidesPerColumnFill: 'row',
    spaceBetween: 30,
    pagination: {
        el: '.sight-pagination',
        bulletClass: "sport-bullet",
        bulletActiveClass: "sport-bullet-active",
        clickable: true,
    },
});
