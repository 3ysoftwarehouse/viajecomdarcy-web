// multiple fields

var blockField = function setPacote(){
  edit = $("#edit-reserva").val()
  if(edit != "true"){
    if($('.form-excursao').val()){
      $('.form-excursao').val(" ");
      $('.form-pacote').val(" ");
      $('.form-acomodacao').val(" ");
      $('.form-preco').val(" ");
    }
  }
  $('.form-pacote').prop('disabled', true);
  $('.form-moeda').prop('disabled', true);
  $('.form-acomodacao').prop('disabled', true);
  $('.form-preco').prop('disabled', true);
  $('.form-opcional').prop('disabled', true);
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
            $("#id_form-"+i+"-id_opcional").select2();
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
            $("#id_form-"+i+"-id_opcional").select2();
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


function setExcursaoPacote(select){
  console.log("setExcursaoPacote")
  var selected = select.options[select.selectedIndex]
  var valor = selected.value
  var id = String(select.id).split('-')[1]
  setPacote(valor,id);
  $("#id_form-"+id+"-id_pacote").parent().children().find('.select2-choice').find('.select2-chosen').html('---------');
  $('#id_form-'+id+'-id_pacote').prop('disabled', false);
  $('#id_form-'+id+'-id_status_reserva option[value="RESERVADO"]').prop('selected', true);
}

function setPacoteAcomodacao(select){
  console.log("setPacoteAcomodacao")
  var selected = select.options[select.selectedIndex]
  var valor = selected.value
  var id = String(select.id).split('-')[1]
  setMoeda(valor,id)
  $("#id_form-"+id+"-id_acomodacao_pacote").parent().children().find('.select2-choice').find('.select2-chosen').html('---------');
  $('#id_form-'+id+'-id_acomodacao_pacote').prop('disabled', false);
}


function setPrecoAcomodacao(select){
  console.log("setPrecoAcomodacao")
  var selected = select.options[select.selectedIndex]
  var valor = selected.value
  var id = String(select.id).split('-')[1]
  $('#id_form-'+id+'-preco_acomodacao').val(selected.getAttribute('data-preco'));
  $('#id_form-'+id+'-preco_acomodacao').prop('disabled', false);
}


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


function setMoeda(codigo,id){
  var url = '/framework/dashboard/reserva/pacote_moeda_json/'+codigo+'/';
  var htmlString = "";
  if(codigo){
    $.ajax({
      url: url,
      type: 'GET',
      success : function(response) { 
        if (response.pacote !== 'error'){

          pacote = response.pacote
          htmlString = '<option selected="selected" value="">---------</option>'
          $('#id_form-'+id+'-reserva_passageiro_preco').val(pacote[0].pacote_preco)
          $("#id_form-"+id+"-id_moeda").html(htmlString+'<option selected="selected" value="'+pacote[0].id_moeda+'">'+pacote[0].id_moeda__moeda_desc+'</option>');
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

function setPassageiroOpcional(select){
  console.log("setPassageiroOpcional")
  var selected = select.options[select.selectedIndex]
  var id_passageiro = selected.value
  var id = String(select.id).split('-')[1]
  var id_reserva = $('#id_reserva').html()
  setOpcional(id, id_reserva, id_passageiro);
  $("#id_form-"+id+"-id_opcional").parent().children().find('.select2-choice').find('.select2-chosen').html('---------');
  $('#id_form-'+id+'-id_opcional').prop('disabled', false);
}

function setOpcional(id, id_reserva, id_passageiro){
  var url = '/framework/dashboard/passageiro/opcional/passageiro_opcional_json/' + String(id_reserva) + "/" + String(id_passageiro);
  $.ajax({
    url: url,
    type: 'GET',

    success : function(response) {
      opicionais = response.opicionais

      var htmlString = '<option selected="selected" value="">---------</option>';
      for(i=0; i < opicionais.length; i++){
        htmlString += '<option value="'+ String(opicionais[i].id_opcional)+'">'+opicionais[i].id_opcional__opcional_desc+'</option>'
      }
      $("#id_form-"+id+"-id_opcional").html(htmlString);

      //var select = document.getElementById("id_form-"+id+"-id_moeda");
      //for(i=0; i<select.options.length; i++){
      //  if(select.options[i].text == response.moeda_desc){
      //    select.options[i].selected = true;
      //  }
      //}

      //htmlString = '<option value="">---------</option>';
      //htmlString += '<option selected="selected" value="'+response.id_moeda+'">'+response.moeda_desc+'</option>';
      //$("#id_form-"+id+"-id_moeda").html(htmlString);

      htmlString = '<option value="">---------</option>';
      htmlString += '<option selected="selected" value="'+response.id_reserva_passageiro+'">'+response.reserva_passageiro_obs+'</option>';
      $("#id_form-"+id+"-id_reserva_passageiro").html(htmlString);

    },

    error: function(error) {
      console.log(error);
    }  

  });
}

function setPassageiroMoedaOpcional(select){
  console.log("setPassageiroMoedaOpcional")
  var selected = select.options[select.selectedIndex]
  var id_opcional = selected.value
  var id = String(select.id).split('-')[1]
  var id_reserva_passageiro = $("#id_form-"+id+"-id_reserva_passageiro").val()
  
  setMoedaOpcional(id, id_reserva_passageiro, id_opcional);
}

function setMoedaOpcional(id, id_reserva_passageiro, id_opcional){
  var url = '/framework/dashboard/passageiro/opcional/passageiro_opcional_moeda_json/' + String(id_reserva_passageiro) + "/" + String(id_opcional);
  $.ajax({
    url: url,
    type: 'GET',

    success : function(response) {
      htmlString = '<option value="">---------</option>';
      htmlString += '<option selected="selected" value="'+response.id_moeda+'">'+response.moeda_desc+'</option>';
      $("#id_form-"+id+"-id_moeda").html(htmlString);
    },

    error: function(error) {
      console.log(error);
    }  

  });
}