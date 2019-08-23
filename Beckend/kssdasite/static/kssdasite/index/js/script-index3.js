$('.more-pr').click(function(){
	if($('.third-block').is(':visible'))
		$('.third-block').hide();
	else $('.third-block').show();
});

$('.menuShow-icon').click(function(){
	if($('.v-menu').is(':visible'))
		$('.v-menu').hide();
	else $('.v-menu').show();
});
