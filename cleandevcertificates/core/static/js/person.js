(function($) {

    $(document).ready(function() {
        // Mask
        $("input#id_cpf").mask("999.999.999-99");

        // Select Kind
        $("select#id_kind").bind("change", function(e) {
            e.preventDefault();

            var $this = $(this);
            var kind = $this.val();
            var cpfFieldRow = $(".field-cpf");
            var universityFieldRow = $(".field-university");
            var courseFieldRow = $(".field-course");
            var semesterFieldRow = $(".field-semester");
            var cityFieldRow = $(".field-city");
            var facebookFieldRow = $(".field-facebook");
            var twitterFieldRow = $(".field-twitter");
            var imageFieldRow = $(".field-image");

            // Hide fields row
            cpfFieldRow.hide(0);
            universityFieldRow.hide(0);
            courseFieldRow.hide(0);
            semesterFieldRow.hide(0);
            cityFieldRow.hide(0);
            facebookFieldRow.hide(0);
            twitterFieldRow.hide(0);
            imageFieldRow.hide(0);

            if(kind == "S") {
                cpfFieldRow.find("label").addClass("required");
                universityFieldRow.find("label").addClass("required");
                courseFieldRow.find("label").addClass("required");
                semesterFieldRow.find("label").addClass("required");

                // Show
                cpfFieldRow.show(0);
                universityFieldRow.show(0);
                courseFieldRow.show(0);
                semesterFieldRow.show(0);
                cityFieldRow.show(0);
                facebookFieldRow.show(0);
                twitterFieldRow.show(0);
            }
            if(["U", "P"].indexOf(kind) > -1) {
                cityFieldRow.find("label").addClass("required");

                imageFieldRow.show(0);
                cityFieldRow.show(0);
            }
        });
        $("select#id_kind").trigger("change");

        // Search Courses by University
        $("select#id_university").change(function() {
            var $this = $(this);
            var course = $("select#id_course");
            var valueCourse = course.val();
            var option = $("<option />");
            var options = [];
            options.push(option.val("").html("---------"));

            if($this.val() != "") {
                $.ajax({
                    url: '/core/courses/courses_by_uniservity/' + $this.val() + '/',
                    type: 'GET',
                    dataType: 'json',
                    success: function(data) {
                        $.each(data, function(i, key) {
                            options.push(
                                option.val(key.pk).html(key.fields.name)
                            );
                        });

                        course.html(options);
                    }
                });
            }

            course.html(options);
            course.val(valueCourse);
        });
        $("select#id_university").trigger("change");
    });

})(django.jQuery);
