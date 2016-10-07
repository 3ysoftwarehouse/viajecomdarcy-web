// multiple fields

    var blockField = function setPacote(){
      edit = $("#edit-reserva").val()
      if(edit != "true"){
        if($('.form-excursao').val()){
          $('.form-excursao').val(" ");
          $('.form-pacote').val(" ");
          $('.form-acomodacao').val(" ");
        }
      }
      $('.form-pacote').prop('disabled', true);
      $('.form-moeda').prop('disabled', true);
      $('.form-acomodacao').prop('disabled', true);
    }

    blockField()


    var lenForm= 1;
    $(function() {
        $('#id_passageiro_table .tr').formset()
        $('.add-row').on('click', function(event) {
            lenForm += 1
            for (i=0; i< lenForm; i++){
                $("#id_form-"+i+"-id_excursao").select2();
                $("#id_form-"+i+"-id_pacote").select2();
                $("#id_form-"+i+"-id_passageiro").select2();
                $("#id_form-"+i+"-id_status_reserva_passageiro").select2();
                $("#id_form-"+i+"-id_acomodacao_pacote").select2();
            }
        });
        $('.delete-row').on('click', function(event) {
            lenForm -= 1
            for (i=0; i< lenForm; i++){
                $("#id_form-"+i+"-id_excursao").select2();
                $("#id_form-"+i+"-id_pacote").select2();
                $("#id_form-"+i+"-id_passageiro").select2();
                $("#id_form-"+i+"-id_status_reserva_passageiro").select2();
                $("#id_form-"+i+"-id_acomodacao_pacote").select2();
            }
        });
    })



    $(function() {
        $("#id_form-0-id_excursao").select2();
        $("#id_form-0-id_pacote").select2();
        $("#id_form-0-id_passageiro").select2();
        $("#id_form-0-id_status_reserva_passageiro").select2();
        $("#id_form-0-id_acomodacao_pacote").select2();
    })


$( ".form-excursao" ).change(function() {
  var excursao = $(this).val()
  var id = $(this).attr('id')
  id = id.split("-")
  id = id[1]
$('.form-pacote').prop('disabled', false);
$("#id_form-"+id+"-id_pacote").parent().children().find('.select2-choice').find('.select2-chosen').html('---------');
setPacote(excursao,id);
});


function setPacote(codigo,id){
  var url = '/framework/dashboard/reserva/pacote_json/'+codigo+'/';
  var htmlString = '<option selected="selected" value="">---------</option>';
  if(codigo){
    $.ajax({
      url: url,
      type: 'GET',
      success : function(response) { 
        if (response.data !== 'error'){
          pacotes = response.data
          for(i=0; i < pacotes.length; i++){
            htmlString += '<option value="'+ String(pacotes[i].id_pacote)+'">'+pacotes[i].pacote_nome+'</option>'
          }
          $("#id_form-"+id+"-id_pacote").html(htmlString);
        }
      },
      error: function(error) {
        console.log(error);
      }    
    });
  }else{
    htmlString = '<option selected="selected" value="">---------</option>'
    $("#id_form-"+id+"-id_pacote").parent().children().find('a').find('.select2-chosen').html("---------")
    $("#id_form-"+id+"-id_pacote").html(htmlString);
    $("#id_form-"+id+"-id_acomodacao_pacote").parent().children().find('a').find('.select2-chosen').html("---------")
    $("#id_form-"+id+"-id_acomodacao_pacote").html(htmlString);
    $('#id_form-'+id+'-reserva_passageiro_preco').val("");
    $('#id_form-'+id+'-id_moeda').val("");
    $('#id_form-'+id+'-reserva_passageiro_cambio').val("");
  }
}


$( ".form-pacote" ).change(function() {
  var pacote = $(this).val()
  var id = $(this).attr('id')
  id = id.split("-")[1]
  setMoeda(pacote,id)
  $(this).prop('selected', true);
  $('.form-acomodacao').prop('disabled', false);
});


$( ".form-acomodacao" ).change(function() {
  var id = $(this).attr('id')
  id = id.split("-")[1]
  console.log($(this).data('preco'))
  $(this).prop('selected', true);
  $('#id_form'+id+'-preco_acomodacao').val($(this).data('preco'));
});


function setMoeda(codigo,id){
  var url = '/framework/dashboard/reserva/pacote_moeda_json/'+codigo+'/';
  var htmlString = "";
  if(codigo){
    $.ajax({
      url: url,
      type: 'GET',
      success : function(response) { 
        if (response.pacote !== 'error'){

          console.log(response)
          pacote = response.pacote

          $('#id_form-'+id+'-reserva_passageiro_preco').val(pacote[0].pacote_preco)
          $("#id_form-"+id+"-id_moeda").html('<option selected="selected" value="'+pacote[0].id_moeda+'">'+pacote[0].id_moeda__moeda_desc+'</option>');
          $('#id_form-'+id+'-reserva_passageiro_cambio').val(pacote[0].id_moeda__moeda_cambio)


          acomodacao = response.acomodacao
          for(i=0; i < acomodacao.length; i++){
            htmlString += '<option data-preco="'+String(acomodacao[i].preco)+'" value="'+ String(acomodacao[i].id_acomodacao)+'">'+acomodacao[i].id_acomodacao__acomodacao_desc+'</option>'
          }
          $("#id_form-"+id+"-id_acomodacao_pacote").html(htmlString);

        }
      },
      error: function(error) {
        console.log(error);
      }    
    });
  }else{
    //htmlString = '<option value=""></option>'
    //$("#id_form-"+id+"-id_pacote").html(htmlString);
  }
}