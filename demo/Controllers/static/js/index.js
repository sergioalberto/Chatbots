$(document).ready(function(){

	$("#mytext").on("keypress", function(event){
		var code = (event.keyCode ? event.keyCode : event.which);
		if (code === 13){
			sendMsj();
		}
	});

	$("#mytext").on("keyup", function(event){
		var code = (event.keyCode ? event.keyCode : event.which);
		if (code === 8){
			// sendMsj();
		}
	});

});

function formatAMPM(date) {
    var hours = date.getHours();
    var minutes = date.getMinutes();
    var ampm = hours >= 12 ? 'PM' : 'AM';
    hours = hours % 12;
    hours = hours ? hours : 12; // the hour '0' should be '12'
    minutes = minutes < 10 ? '0'+minutes : minutes;
    var strTime = hours + ':' + minutes + ' ' + ampm;
    return strTime;
}

//-- No use time. It is a javaScript effect.
function insertChat(who, text, time){
    if (time === undefined){
        time = 0;
    }
    var control = "";
    var date = formatAMPM(new Date());

    if (who == "you"){
        control = '<li style="width:100%" class="another-person">' +
                        '<div class="msj macro">' +
                        '<div class="avatar"><img class="img-circle" style="width:50px;" src="'+ me.avatar +'" /></div>' +
                            '<div class="text text-l">' +
                                '<p>'+ text +'</p>' +
                                '<p><small>'+date+'</small></p>' +
                            '</div>' +
                        '</div>' +
                    '</li>';
    }else{
        control = '<li style="width:100%;" class="another-person">' +
                        '<div class="msj-rta macro">' +
                            '<div class="text text-r">' +
                                '<p>'+text+'</p>' +
                                '<p><small>'+date+'</small></p>' +
                            '</div>' +
                        '<div class="avatar" style="padding:0px 0px 0px 10px !important"><img class="img-circle" style="width:50px;" src="'+you.avatar+'" /></div>' +
                  '</li>';
    }
    setTimeout(
        function(){
            $("ul").append(control).scrollTop($("ul").prop('scrollHeight'));
        }, time);

}

function resetChat(){
    $("ul").empty();
}

function sendMsj(){
	var text = $("#mytext").val();
	if (text !== ""){
		insertChat("me", text);
		$("#mytext").val('');
	}
}
