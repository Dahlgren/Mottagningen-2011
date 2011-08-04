jQuery.noConflict();

jQuery(document).ready(function($) {
    jQuery.getJSON('timeedit/events.json', function(data) {
        jQuery.each(data, function(key, events) {
            var $day = jQuery('#' + key);
            var $listdom = $day.find('ul');
            jQuery.each(events, function(index, value) {
                var str = "<li><span class='time'>" + value.start + "</span> - " + value.title;
                
                if (value.location)
                    str += "<br/>" + value.location + "</li>";
                                
                $listdom.append(str);
            });
        });
    });
});