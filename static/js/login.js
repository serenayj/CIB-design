$(document).ready(function () {

	$('#signin').click(function(event){
		event.preventDefault();
		var loginurl = "http://127.0.0.1:8000/index/";
            $.ajax({
                 type:"POST",
                 url:loginurl,
                 data :$("#mainform").serialize();
                 success:function(response){
                 	window.location = response;
                 	alert("login success!")
                 },                
                                                                                                                                        
       });

    });

    $('#signup').click(function(){
    	$.ajax({
            type : "POST",
            url:"registration.html",
            success:function(data){
                window.open()
                alert("you are directing to registration!")
            }
        })
    })
});
