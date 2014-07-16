(function($) {
    $('ul.nav-tabs a[href="' + window.location.pathname + '"]').parent("li").addClass("active");

    $("button.close").click(function() {
        $(this).parent("#result").removeClass("show");
    });

})(django.jQuery);
