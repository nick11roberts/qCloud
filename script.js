var reservedWords = ["qubit", 'H', "pX", "pY", "pZ", "pShift", "read"];
var xmlhttp = new XMLHttpRequest();
var URL = "http://localhost:5000/";

xmlhttp.onreadystatechange = function() {
    console.log("readyState = " + xmlhttp.readyState);
    console.log("status = " + xmlhttp.status);
    if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
      
        if (xmlhttp.responseText != null) {
            reply = JSON.parse(xmlhttp.responseText);
            process(reply);
        }
        console.log(xmlhttp.responseText);
    }
}

function getInput(ele) {
    document.getElementById("errorMessage").innerHTML = "";
    if(event.keyCode == 13) {
        for(var i = 1; i <= 3; i++){
            document.getElementById("img"+i).src = "https://upload.wikimedia.org/wikipedia/commons/2/26/Microchip_PIC24HJ32GP202.jpg";
        }
        if (ele.value == "")
            return;
        var inputStr = ele.value;
        ele.value = "";
        var result = validation(inputStr);
        console.log(result);
        if (result["bool"]) {
            // Send data to server
            xmlhttp.open("POST", URL, true);
            xmlhttp.send(JSON.stringify(inputStr));
            return;
        }
        //print out user error
        document.getElementById("errorMessage").innerHTML = result["error"];
        document.getElementById("errorMessage").style.font = "bold 20px arial, serif";
        document.getElementById("errorMessage").style.color = "orange";
        document.getElementById("errorMessage").style.backgroundColor = "grey";
    }        
}

function validation(str) {
    var arr = str.split(' ');
    var result = {};
    if (reservedWords.indexOf(arr[0]) != -1) {
        if (arr[0] == "pShift") {
            var reserve = reservedWords.indexOf(arr[1]) == -1;
            result["error"] = reserve ? "" : arr[1] + " is a reserved syntax. ";
            var containNum = isNaN(parseFloat(arr[1]));
            result["error"] += containNum ? "" : arr[1] + " does not follow variable naming convention. ";
            var number = (/^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?$/.test(arr[2]));
            result["error"] += number ? "" : arr[2] + " is not a number";
            result["bool"] = reserve && containNum && number;
            //return (reservedWords.indexOf(arr[1]) == -1) && isNaN(parseFloat(arr[1])) && (/^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?$/.test(arr[2]));
            return result;
        }
        var reserve = reservedWords.indexOf(arr[1]) == -1;
        result["error"] = reserve ? "" : arr[1] + " is a reserved syntax. ";
        var containNum = isNaN(parseFloat(arr[1]));
        result["error"] += containNum ? "" : arr[1] + " does not follow variable naming convention. ";
        result["bool"] = reserve && containNum;
        return result;
    }
    return {"bool": false, "error": arr[0] + " is an invalid syntax"};
}


// $(document).ready(function() {
//     $("#demo").on("hide.bs.collapse", function(){
//         $(".btn").html('<span class="glyphicon glyphicon-collapse-down"></span> Open');
//     });
//     $("#demo").on("show.bs.collapse", function(){
//         $(".btn").html('<span class="glyphicon glyphicon-collapse-up"></span> Close');
//     });
//     $('body').scrollTo('#end');
// });
