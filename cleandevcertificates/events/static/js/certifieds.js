(function($) {

    $(document).ready(function() {
        // -->
        // Send token for certified
        $("input#id_token").focus(function() {
            $("div#errors").hide(0).html("");
        });

        // Form Certified
        $("form#id_form_certified").submit(function() {
            var $this = $(this);
            var token = $("input#id_token");
            var error_message = '<br><p class="alert alert-danger"><strong>Opss..</strong><br> Este token pode estar expirado ou inválido.</p>';
            var success_message = '<p class="alert alert-success">Seu certificado foi emitido com sucesso e enviado para o seu e-mail cadastrado. Obrigado.</p>';

            if(token.val() == "") {
                $("div#errors").html(error_message).show();
                return false;
            }

            $.ajax({
                url: $this.attr("action"),
                type: 'POST',
                data: $this.find('input'),
                dataType: 'json',
                statusCode: {
                    300: function(data) {
                        window.location = data.responseText;
                    },
                    404: function(data) {
                        $("div#errors").html(error_message).show();
                    }
                }
            });

            return false;
        });

        $('form#id_rating > label').click(function() {
            rating($(this));
        });

        $('form#id_rating textarea').keyup(function() {
            rating();
        })
        .blur(function() {
            rating();
        });
    });

    //
    function rating(element) {
        var formRating = $("form#id_rating");
        var ratings = $('form#id_rating > label');
        var rating = formRating.find("input#id__rating");

        if(element) {
            var $this = $(element);
            var rating = $this.find("input[name=rating]");
            formRating.find("input#id__rating").val(rating.val());
        }

        $.ajax({
            url: formRating.attr("action"),
            type: formRating.attr("method"),
            data: {
                'csrfmiddlewaretoken': formRating.find("input[name=csrfmiddlewaretoken]").val(),
                '_action': formRating.find("input[name=_action]").val(),
                'rating': rating.val(),
                'observation': formRating.find("textarea[name=observation]").val(),
            },
            dataType: "json",
            statusCode: {
                200: function(data) {
                    ratings.removeClass("glyphicon-star")
                           .addClass("glyphicon-star-empty")
                           .find('input').removeAttr("checked");

                    var i = 0;
                    ratings.each(function() {
                        i++;

                        if (rating.val() >= i) {
                            $(this).removeClass("glyphicon-star-empty")
                                   .addClass("glyphicon-star");
                        }

                        if (rating.val() == i) {
                            $(this).find("input").attr("checked", "checked");
                        }
                    });

                    formRating.find("#result")
                    .addClass("show")
                    formRating.find("#result > p").html("Obrigado por avaliar este evento.");
                }
            }
        });
}

})(django.jQuery);
