$(function() {
    function equalHeight(group) {
        var tallest = 0;
        group.each(function() {
            var thisHeight = $(this).height();
            if (thisHeight > tallest) {
                tallest = thisHeight;
            }
        });
        group.height(tallest);
    }
    equalHeight($(".box-1 .inner"));

    $("#tags4").autocomplete({
        minLength: 3,
        source: function(req, add) {
            var search = $("#tags4").val();
            $.ajax({
                url: '/con_ajax_cadena/',
                async: false,
                dataType: 'json',
                type: 'GET',
                data: { 'start': search, },
                success: function(data) {
                    var suggestions = [];

                    $.each(data, function(index, objeto) {
                        suggestions.push(objeto.first_name);
                    });

                    add(suggestions);
                },
                error: function(err) {
                    alert("error");
                }
            });
        }
    });
});
