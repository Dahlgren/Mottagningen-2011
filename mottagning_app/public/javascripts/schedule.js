var days;
var headerDays;
var headerHeight;

jQuery.noConflict();

function select(index){
	headerDays.removeClass("active");
	headerDays.eq(index).addClass("active");
	
	days.removeClass("active");
	days.eq(index).addClass("active");	
}

function checkPosition(pos) {
	dayIndex = 0;

	jQuery.each(days, function(index, value) {
		if (jQuery(value).offset().top - headerHeight < pos) {
			dayIndex = index;
		}
	});
	
	return dayIndex;
}

function handleScroll(pos) {
	index = checkPosition(pos)
	select(index);
}

jQuery(document).ready(function($) {
	headerHeight = $('#header').height();
	
	headerDays = $('div#header div#days li');
	days = $('div#schedule div.day div.date');
		
	headerDays.click(function () {
		index = headerDays.index($(this));
		pos = days.eq(index).offset().top - headerHeight - days.eq(index).height() + 10;
		$.scrollTo(pos, "normal");
	});
	
	 $(window).scroll(function(){
	 
		var y = window.scrollY + headerHeight;
		handleScroll(y);
	});
	
	select(0);
});