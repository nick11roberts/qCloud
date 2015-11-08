var reservedWords = ["qubit", 'H', "pX", "pY", "pZ", "pShift", "read"];
var xmlhttp = new XMLHttpRequest();
var URL = "http://localhost:5000/";

xmlhttp.onreadystatechange = function() {
    console.log("readyState = " + xmlhttp.readyState);
    console.log("status = " + xmlhttp.status);
    if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
        // console.log("fdsJFADSKd");
        console.log(xmlhttp.responseText);

        // if (xmlhttp.responseText == 1 || xmlhttp.responseText == "1") {
        //     console.log("success");
        //     console.log(xmlhttp.responseText);

        // }
        // else if (xmlhttp.responseText == undefined || !(xmlhttp.responseText) || xmlhttp.responseText == "None") {
        //     console.log("success but undefined");
        // }
        // else if (/^[\],:{}\s]*$/.test(xmlhttp.responseText.replace(/\\["\\\/bfnrtu]/g, '@').
        //     replace(/"[^"\\\n\r]*"|true|false|null|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?/g, ']').
        //     replace(/(?:^|:|,)(?:\s*\[)+/g, ''))) {
        if (reply != null) {
            reply = JSON.parse(xmlhttp.responseText);
            process(reply);
        }
    	   // if (reply != null){
    	   // 	   // do stuff//
        // 	   	console.log("success");
        //         console.log(reply);
        // 	}
        // }
        console.log(xmlhttp.responseText);
    }
}
function process(arrayName) {
    
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
    	if (validation(inputStr)) {
       		// Send data to server
        	xmlhttp.open("POST", URL, true);
        	xmlhttp.send(JSON.stringify(inputStr));
    		return;
    	}
        //print out user error
        document.getElementById("errorMessage").innerHTML = "Invalid Syntax";
        document.getElementById("errorMessage").style.font = "italic bold 20px arial,serif"
    }
}

function validation(str) {
	var arr = str.split(' ');
    if (reservedWords.indexOf(arr[0]) != -1) {
		if (arr[0] == "pShift")
    		return (reservedWords.indexOf(arr[1]) == -1) && isNaN(parseFloat(arr[1])) && (/^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?$/.test(arr[2]));
    	return (reservedWords.indexOf(arr[1]) == -1) &&  isNaN(parseFloat(arr[1]));
    }
	return false;
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
