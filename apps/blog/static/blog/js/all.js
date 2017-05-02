$(document).ready(function () {
	
	// fancybox
	jQuery('.fancybox').fancybox();
	// input mask
	$(".input[name='phone']").mask("+7 (999) 999 99 99");
	// validation
	$('form').each(function(){
		$(this).validate({
			   rules: {
				name: {
					required: true,
					minlength: 3
				},
				mail: {
					required: true,
					email: true
				},
				phone: {
					required: true,
					minlength: 3
				}
			}
	    });
	});
	// header langs
	$(document).on('click','.lang-top',function(e){
		e.preventDefault();
		if($(this).hasClass('active')){
			$(this).removeClass('active');
			$('.lang-hidden').slideUp();
		}else{
			$(this).addClass('active');
			$('.lang-hidden').slideDown();
		}	
	});
	
	// header langs
	$(document).on('click','.nav-icon',function(e){
		e.preventDefault();
		$('.header-line').slideDown();
	});
	$(document).on('click','.nav-close',function(e){
		e.preventDefault();
		$('.header-line').slideUp();
	});
	
	
});
$(window).load(function(){
	// review align
	$('.blog-list').masonry({
		// options
		columnWidth: '.blog-sizer',
		gutter: '.gutter-sizer',
		itemSelector: '.blog-item',
		percentPosition: true
		
	});
	$('.langs-link a').click(function(){
    var url = $(this).parents('.header-lang').data('url');
    console.log(url);
    var csrfmiddlewaretoken = $('.header-lang input[name=csrfmiddlewaretoken]').val();
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
