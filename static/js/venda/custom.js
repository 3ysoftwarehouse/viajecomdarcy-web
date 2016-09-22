$( ".form-excursao" ).change(function() {
  var excursao = $(this).val()
  var id = $(this).attr('id')
  id = id.split("-")
  id = id[1]

setPacote(excursao,id);

});


function setPacote(codigo,id){
    
    
   var url = '/framework/dashboard/reserva/pacote_json/'+codigo+'/';
   var htmlString = "";
   if(codigo){
      $.ajax({
          url: url,
          type: 'GET',
         success : function(response) { 
          if (response.data !== 'error'){
              pacotes = response.data
              for(i=0; i < pacotes.length; i++){
                htmlString += '<option value="'+pacotes[i].id_pacote+'">'+pacotes[i].pacote_nome+'</option>'
                $("#id_form-"+id+"-id_pacote").html(htmlString);
              }
          }
      },
          error: function(error) {
          console.log(error);
          }    
      });
    }else{
      htmlString = '<option value=""></option>'
      $("#id_form-"+id+"-id_pacote").html(htmlString);
    }
}