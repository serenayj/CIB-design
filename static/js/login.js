$(document).ready(function () {

	$('#signin').click(function(event){
		event.preventDefault();
            $.ajax({
                 type:"POST",
                 url:"/login/",
                 data : $(this).serialize(),
                 success:function(response){

                 }

                                                                                                                                        
       });

    });

    $('#signup').click(function(){
    	('#registration').removeClass('style');
    })