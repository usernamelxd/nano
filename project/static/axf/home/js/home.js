$(document).ready(function(){
    swiper1()
    swiper2()
});

function swiper1(){
    var swiper = new Swiper('#topSwiper',{
        direction:"horizontal",//水平轮播
        loop: true, //是否自动
        speed: 500,
        autoplay: 2000,
        pagination:{
            el:".swiper-pagination",

        }

    })
}

function swiper2(){
    var swiper = new Swiper("#menuSwiper",{
        slidesPerViw: 3, //一页有三个
        spaceBetween: 2, //中间间隔2像素
        loop: false,

    });
}