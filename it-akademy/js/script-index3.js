$('.more-pr').click(function(){
	if($('.third-block').is(':visible'))
		$('.third-block').hide();
	else $('.third-block').show();
});

$('.fa-search').click(function(){
	if($('.none-flex-search').is(':hidden'))
		$('.none-flex-search').show();
	else $('.none-flex-search').hide();
});


$('.fa-bars').click(function(){
	if($('.mobilMenu').is(':hidden'))
		$('.mobilMenu').show();
	else $('.mobilMenu').hide();
});



  $(function() {
  $('.more-pr').on('click', function(e) {
    e.preventDefault();
    $('html, body').animate({ scrollTop: ($('.third-block').offset().top)-70}, 500, 'linear');
  });
});

