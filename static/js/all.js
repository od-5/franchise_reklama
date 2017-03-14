$(document).ready(function () {

  // fancybox
  jQuery('.fancybox').fancybox();
  // popup close
  $(document).on('click','.popup-close',function(e){
    e.preventDefault();
    $.fancybox.close();
  });

  $(".input[name='phone']").mask("+7 (999) 999-99-99");
  $('form').each(function(){
    $(this).validate({
         rules: {
        name: {
          required: true,
          minlength: 3
        },
        phone: {
          required: true,
          minlength: 3
        },
        mail: {
          required: true,
          email: true
        }
      }
      });
  });

  // fake-select hidden
  $(document).on('click', '.city-region-link', function(e){
    e.preventDefault();
    if($(this).hasClass('active')){
      $('.city-region-block').slideUp();
      $(this).removeClass('active');
    }else{
      $('.city-region-block').slideDown();
      $(this).addClass('active');
    }
  });
  $(document).bind( "mouseup touchend", function(e){
    var container = $('.fake-select-hidden, .fake-select-link');
    if (!container.is(e.target) // if the target of the click isn't the container...
      && container.has(e.target).length === 0) // ... nor a descendant of the container
    {
      $('.fake-select-hidden').slideUp();
      $('.fake-select-link').removeClass('active');
    }
  });

  // button info
  $(document).on('click','.button-data',function(e){
    e.preventDefault();
    var data_title = $(this).attr('data-title');
    var data_theme = $(this).attr('data-theme');
    $('#popup input[name=theme]').val(data_theme);
    $('#popup .insert-title').text(data_title);
  });

  // slider
  $('.review-slider .owl-carousel').owlCarousel({
    loop: true,
    items: 1,
    nav: true,
    dots: false,
    //autoHeight : true,
    navText: [''],
    autoplay: false
  });

  $('.langs-link a').click(function(){
    var url = $(this).parents('.header-langs').data('url');
    console.log(url);
    var csrfmiddlewaretoken = $('.header-langs input[name=csrfmiddlewaretoken]').val();
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
});

