$('.more-pr').click(function(){
	if($('.third-block').is(':visible'))
		$('.third-block').hide();
	else $('.third-block').show();
});

$('.fa-bars').click(function(){
	if($('.v-menu').is(':visible'))
		$('.v-menu').hide();
	else $('.v-menu').show();
});

$('.fa-search').click(function(){
	if($('.search-control').is(':visible'))
		$('.search-control').hide();
	else $('.search-control').show();
});
