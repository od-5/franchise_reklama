jQuery(function($){
  //$('.link a').hover(function() {
  //  $('.ipad').toggleClass( 'top' )
  //});

  // Выбор языка
  $('.languages-list').hover(function(){
    $(this).toggleClass('active')
  });
  $('.languages-list a').click(function(){
    var url = $(this).parents('.languages-list').data('url');
    console.log(url);
    var csrfmiddlewaretoken = $('.languages-list input[name=csrfmiddlewaretoken]').val();
    console.log(csrfmiddlewaretoken);
    var language = $(this).data('language');
    console.log(language);
    $.ajax({
      type: "POST",
      url: url,
      data: {
        language: language,
        csrfmiddlewaretoken: csrfmiddlewaretoken
      },
      success: function(){
        location.reload();
      }
    });
  });


  $('.fancybox').fancybox({
            padding : 0,
        });

  $('.ticket_form').each(function(){
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
  //$('.ticket_form').ajaxForm({
  //  success: function(data){
  //    if (data.success) {
  //      $('.ticket_form').resetForm();
  //      $.notify(data.success, 'success');
  //    } else {
  //      $.notify(data.success, 'error');
  //      $('.ticket_form').resetForm();
  //    }
  //  }
  //});


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
