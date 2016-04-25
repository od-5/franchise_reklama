jQuery(function($){
  $('.link a').hover(function() {
    $('.ipad').toggleClass( 'top' )
  });

  $('.languages-list').click(function(){
    $(this).toggleClass('active')
  });

  $('.fancybox').fancybox({
            padding : 0,
        });

  $('form').each(function(){
    $(this).validate({
      rules: {
        name: {
          required: true
        },
        mail: {
          required: true,
          email: true
        },
        phone: {
          required: true,
          minlength: 6
        }
      }
    });
  });
  $('form').ajaxForm({
    success: function(data){
      if (data.success) {
        $('form').resetForm();
        $.notify(data.success, 'success');
      } else {
        $.notify(data.success, 'error');
        $('form').resetForm();
      }
    }
  });


  $(window).scroll(function(){
    if ($(this).scrollTop() > 100) {
      $('nav').addClass('nav');
    } else {
      $('nav').removeClass('nav');
    };

    var t = $(this).scrollTop() + 275;
    var sid;
    $('nav .scroll').each(function(){
      var id = $(this).attr('href').replace('/', '');
      var o = $(id).offset().top;
      if(o < t){
        sid = id;
      }
    });
    $('nav .scroll').removeClass('active');
    if(sid){
      $('nav [href="'+sid+'"]').addClass('active');
    }
  });
  $("[name='phone']").mask("+7 (999) 999-99-99");

  $('nav .scroll').click(function(){
    var el = $(this).attr('href');
    $('body').animate({
    scrollTop: $(el).offset().top}, 2000);
    return false;
  });


});
