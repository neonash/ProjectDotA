(function() {
    $("#main-panel").addClass('hidden');
    $('#refresh-data').addClass('hidden');
    $('#search').addClass('active');


    var searchQuery = null;

    //Read the requests from the request queue
    $.get('/service/getData/').then(function (successResponse) {

        // console.log('Stringify successResponse', JSON.stringify(successResponse));
        console.log('Parsed successResponse', JSON.parse(successResponse));
//        var clients = [
//            { "Request ID": "001", "Product": "TV", "Time": "16:54 Feb 20th 2016" , "Status": "Completed"},
//            { "Request ID": "002", "Product": "iMac", "Time": "20:01 April 10th 2016" ,"Status": "Completed"},
//            { "Request ID": "003", "Product": "iPad", "Time": "15:41 January 31st 2017" ,"Status": "Processing"},
//            { "Request ID": "004", "Product": "iPhone", "Time": "13:09 February 15th " ,"Status": "Pending"},
//            { "Request ID": "005", "Product": "Chrome Book" , "Time": "00:45 February 21st" ,"Status": "Pending"}
//        ];
//         var $table = $('#boot-table');
//         var mydata =
//         [
//             {
//                 "id": 0,
//                 "name": "test0",
//                 "price": "$0"
//             },
//             {
//                 "id": 1,
//                 "name": "test1",
//                 "price": "$1"
//             },
//
//         ];
//
//         $(function () {
//             $('#boot-table').bootstrapTable({
//                 data: mydata
//             });
//         });
        //This function is used to populate jsGrid div to load contents of requests queue from DB
    function JSONToCSVConvertor(JSONData, ReportTitle, ShowLabel) {

        //If JSONData is not an object then JSON.parse will parse the JSON string in an Object
        var arrData = typeof JSONData != 'object' ? JSON.parse(JSONData) : JSONData;
        var CSV = '';
        //This condition will generate the Label/Header
        if (ShowLabel) {
            var row = "";

            //This loop will extract the label from 1st index of on array
            for (var index in arrData[0]) {
                //Now convert each value to string and comma-seprated
                row += index + ',';
            }
            row = row.slice(0, -1);
            //append Label row with line break
            CSV += row + '\r\n';
        }

        //1st loop is to extract each row
        for (var i = 0; i < arrData.length; i++) {
            var row = "";
            //2nd loop will extract each column and convert it in string comma-seprated
            for (var index in arrData[i]) {
                row += '"' + arrData[i][index] + '",';
            }
            row.slice(0, row.length - 1);
            //add a line break after each row
            CSV += row + '\r\n';
        }

        if (CSV == '') {
            alert("Invalid data while downloading");
            return;
        }
        else{
            return(CSV);
        }
    }

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
//             rowClick: function(args) {
// //                console.log($(args.event.target).closest("a"));
//                 // save selected item
//                 selectedItem = args.item;
//                 // save selected row
//                 $selectedRow = $(args.event.target).closest("tr");
//                 $selectedCell = $(args.event.target).closest("a");
//                 $selectedCellClass = $(args.event.target).closest("a").attr("class");
// //                console.log($selectedCell);
//                 // add class to highlight row
//                 $selectedRow.addClass("selected-row");
// //                console.log(selectedItem);
// //                console.log(selectedItem.reqKw);
//
//
//             },
        });
    }, function (errorResponse) {
            console.log("errorResponse", errorResponse)
    });


    // $("#btnPredict").click(function(e){
    //     var data = $("#jsGrid").jsGrid("option", "data");
    //     console.log(data);
    //     $.post('/service/getData/').then(function (successResponse) {
    //
    //     }, function (errorResponse) {
    //         console.log("errorResponse", errorResponse)
    //     });
    // });

    $('#btnPredict').on('click', function (e) {
    //console.log("Button clicked");
    //var refresh = window.urlUtils.getQueryParameter(window.location.href, 'refresh');
    //console.log(refresh);
    var data = $("#jsGrid").jsGrid("option", "data");
    console.log(data);
    var type = null;
    var url= null;
    var match_id =  Math.random().toString(36).substring(2,6) + Math.random().toString(36).substring(2, 6);
    $.ajax({
        type : 'POST',
        url : "/service/pushData/",
        headers: {
            'X-CSRFToken': $.cookie('X-CSRFToken')
        },
        data:  {'match_id_hash': match_id , 'records': JSON.stringify(data)},
        success: function(response) {
            // alert("Request raised succesfully");
//                                    alert(JSON.stringify(tag_dict));
            console.log("Prediction value=", response);
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
        failure: function(response) {
            alert("Failure")
        }
    });
    //console.log("Ajax call request = ", query)
});


    $('.jsgrid-grid-body').css('height', '100%');
    }
    )();