window.addEventListener("scroll", function(event) {
    var top = this.scrollY,
        left =this.scrollX;
    
    
    if(top>($(window).height()/2)){console.log("TOP : "+top+" LEFT : "+left);
                                  $("nav").removeClass("classical-nav");
                                   $("nav").addClass("masked-nav");
                                   $("#arcane-logo").attr("src","ruby.png");
                                  }
    else{
        $("nav").removeClass("masked-nav");
        $("nav").addClass("classical-nav");
        $("#arcane-logo").attr("src","logo_fit.png");
    }
}, false);

$(document).ready(function(){
    $('.modal').modal();
  });