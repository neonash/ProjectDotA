(function() {
    $("#main-panel").addClass("hidden");
    $("#refresh-data").addClass("hidden");
    $("#search").addClass("active");

    //Read the requests from the queue
    $.get("/service/getData/").then(function (successResponse) {

        $("#jsGrid").jsGrid({
            width: "100%",
            height: "400px",

            inserting: false,
            editing: true,
            sorting: true,
            paging: true,
            autoload: true,
            selecting:true,
            pageLoading: true,
            loadIndication: true,
            loadMessage: "Please, wait...",

            data: JSON.parse(successResponse),

            fields: [
                //{ name: "match_id_hash", type: "text", width: 40, title:"Match ID" },
                { name: "player", type: "text", width: 10, title: "Player" },
                { name: "gold", type: "text", width: 10, title: "Gold" },
                { name: "xp", type: "text", width: 10, title: "Exp" },
                { name: "health", type: "text", width: 10, title: "Health" },
                { name: "level", type: "text", width: 10, title: "Level" },
                { name: "hero_id", type: "text", width: 10, title: "Hero_ID" },
                { type: "control" }


            ]

        });
    }, function (errorResponse) {
    });


    $("#btnPredict").on("click", function (e) {

    var data = $("#jsGrid").jsGrid("option", "data");
    var type = null;
    var url= null;
    var matchId =  Math.random().toString(36).substring(2,6) + Math.random().toString(36).substring(2, 6);
    $.ajax({
        type : "POST",
        url : "/service/pushData/",
        headers: {
            "X-CSRFToken": $.cookie("X-CSRFToken")
        },
        data:  {"match_id_hash": matchId , "records": JSON.stringify(data)},
        success(response) {
            if(response>0.5){
                $( ".card-body a" ).text("Radiant");
                $( ".card-body p" ).text("With a Win (%) Probability of :");
                $( "#card-probability" ).text((Math.floor(response* 10000) / 100));
            }
            else{
                $( ".card-body a" ).text("Dire");
                $( ".card-body p" ).text("With a Win (%) Probability of :");
                $( "#card-probability" ).text((100 - Math.floor(response* 10000) / 100));

            }


        },
        failure() {
            alert("Failure");
        }
    });
});


    $(".jsgrid-grid-body").css("height", "100%");
}
)();