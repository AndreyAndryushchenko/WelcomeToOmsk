new WOW().init()

var swiperSport = new Swiper('.swiper-container-sport', {
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

var swiper = new Swiper('.swiper-container-sight', {
  loop: true,
});
