$(document).ready(function () {

  $(function() {
    $( "#tabs1" ).tabs();
  });
  
	$('#search').click(function(){

		$('#tabs-1').fadeOut('normal');
		$('#tabs-2').fadeOut('normal');
	
		var shopstyle = "http://api.shopstyle.com/api/v2/products?pid=uid7556-29692666-0&fts="+$("#query").val()+"&offset=0&limit=10";
			//shopstyle = "http://api.shopstyle.com/api/v2/products?pid=YOUR_API_KEY&fts=red+dress&offset=0&limit=10"
		$.ajax({
			type :"get",
			url : shopstyle,
			dataType: "json",
			success: function(data){
			
				$('#productlist').html(''); // clear the div's html contents for each time the query is processed
					for(var i=0; i< data['products'].length; i++) {
						var pre_append_text = '<div class=col-sm-6 col-md-3><div class=thumbnail><div class=caption>'
                        	+'<img src='+data['products'][i]['image']['sizes']['Best']['url']+ ' draggable=true>'
                         	+'<h5>'+ data['products'][i]['brandedName']+ '</h5></div></div></div>';
					
							
				//append the product's name into the div as list elements
						$('#catalog').append(pre_append_text);
						
						$(function() {
							// below is the problem statement, its scope needs to be strictly defined.
							$( "#catalog .caption" ).draggable({
									appendTo: "body",
									helper: "clone"
								});
							});
						}
					}
			});
		});
		
		$(function() {
			//set item to be draggable
				$( "#catalog li" ).draggable({
					appendTo: "body",
					helper: "clone"
					
				});
				//set item to be droppable
				$( "#cart ul" ).droppable({
					activeClass: "ui-state-default",
					hoverClass: "ui-state-hover",
					accept: ":not(.ui-sortable-helper)",
					drop: function( event, ui ) {
						markImage(ui.draggable.clone());
						$('#mytext').toggle('slow');
						$('#comment').toggle('slow',function(){
							commentShow();
						});
						$('#ratings').toggle('slow',function(){
							ratingsShow();
						});
						console.log(this);
						
					//$( this ).find( ".placeholder" ).remove();
					//$( "<li></li>" ).content( ui.draggable.content() ).appendTo( this );
				  }
				}).sortable({
				  items: "li:not(.placeholder)",
				  sort: function(){
					// gets added unintentionally by droppable interacting with sortable
					// using connectWithSortable fixes this, but doesn't allow you to customize active/hoverClass options
					$( this ).removeClass( "ui-state-default" );
				  }
				});

				//drag items to the board and items will be fixed size
				function markImage($item){
					$item.fadeOut("slow",function(){
						$item.find(".placeholder").remove()
						.end()
						.css("width","80px")
						.appendTo(this)
						.find("img")
							.css("height","72px")
						.end()
						.clone()
						.appendTo('.placeholder')
						.fadeIn();
						
					})
				}

				function commentShow(){
					function handler(event){
						$('#comment').click(function(){
							//working on comment box, referenced from jsfiddle
							var commenttext = "<div id='msgbox'><p>Please enter any additional comments:</p><textarea id='ta' rows='5' cols='30'></textarea>"
							var target = $("#mytext").val();
							$('#itemcomment').html(commenttext);
							$('#msgbox').dialog({
								autoOpen:false,
								modal:true,
								title: 'Add Comments',
								buttons: {
									Okay: function() {
										var oldComments = $("#theDescription").html();
										var newComments = $('#ta').val();
										$('p.comment').html(oldComments +'<br />' + newComments);

            //Do your ajax update here:
            /*
            $.ajax({
                //Unsure of cfc syntax
            });
							*/
										$(this).dialog('close');
									},
							Cancel: function() {
								$(this).dialog('close');
							}
							},
						close: function() {
							alert('AJAX update completed');
						}
						});
							$('#msgbox').dialog('open');
							//});
						});
                    }
				$('button').click(handler).find('button').hide();
			}

				function ratingsShow(){
					var testhtml = "<input id='input-2ba' type='number' class='rating' min='0' max='5' step='0.5'data-stars=5 data-size='xs' data-symbol='&#xe005;' data-default-caption='{rating} hearts' data-star-captions='{}'/>"
					$(this).after(testhtml);
				}
		});
	});