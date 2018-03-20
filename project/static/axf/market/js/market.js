$(document).ready(function(){
    //黄色小方块
    var urlstr = location.href;
    arr = urlstr.split("/");
    $span = $(document.getElementById(arr[4]));
    $span.addClass("yellowSlide");

    $("#alltypebtn").bind("click",function(){
        $("#typeDiv").toggle()
        $("#sortDiv").hide()
    });
    $("#sortbtn").bind("click",function(){
        $("#typeDiv").hide()
        $("#sortDiv").toggle()
    });
    
    function selfhide() {
        $(this).hide()
    }
    $("#typeDiv").bind("click",selfhide());
    $("#sortDiv").bind("click",selfhide())
    

});