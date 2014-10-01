$("#flag-submission").click(function() {

    var cat = $(".task-box").data("category");
    var score = $(".task-box").data("score");
    var flag = $("#flag-input").val();

    console.log("/submit/" + cat + "/" + score + "/" + btoa(flag));

    $.ajax({
        url: "/submit/" + cat + "/" + score + "/" + btoa(flag)
    }).done(function(data) {

        console.log(data);

        if (data["success"]) {
            $("#flag-input").val($(".lang").data("success"));
            $("#flag-submission").removeClass("btn-primary");
            $("#flag-submission").addClass("btn-success");
            $("#flag-submission").attr('disabled','disabled');
        } else {
            $("#flag-input").val($(".lang").data("failure"));
        }
    });
});