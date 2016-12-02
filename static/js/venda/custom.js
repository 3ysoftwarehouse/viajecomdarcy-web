// multiple fields

function getCookie(name) {
 var cookieValue = null;
 if (document.cookie && document.cookie != '') {
   var cookies = document.cookie.split(';');
   for (var i = 0; i < cookies.length; i++) {
     var cookie = jQuery.trim(cookies[i]);
     if (cookie.substring(0, name.length + 1) == (name + '=')) {
       cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
       break;
     }
   }
 }
 return cookieValue;
}

function finalizarAgendamento(){
    id_cliente = $("#id_id_cliente").val()
    $.ajax({
        url: url_finalizar + id_reserva + '/' + id_cliente + '/',
        type: 'GET',
        success: function(response){
          if (response.status == "success"){
            window.location = url_list;
          }else{
            console.log(response.message);
          }
        }
    })
}

function genNotification(message,type){

    $('body').pgNotification({
        style: 'bar',
        message: message,
        position: 'top',
        timeout: 2000,
        type: type
    }).show();
}    


$('#new_reserva_passageiro_btn').on('click', function(event) {
  $('#form-personal').validate();
  var csrftoken = getCookie('csrftoken');
  if($('#form-personal').valid()){
    var formData = new FormData($('#form-personal')[0]);
    formData.append('csrfmiddlewaretoken', csrftoken);
    $.ajax({
      url: url,
      type: 'POST',
      enctype: "multipart/form-data",
      cache: false,
      contentType: false,
      processData: false,
      data: formData,
      success : function(response) {
        if(response.status == "success"){
        genNotification('Passageiro adicionado com sucesso!','success');
        $('#divDetalhes').html(response.html);
        }
        else{
          genNotification(response.message,'error');
        }
        $('#modalPassageiro').modal('hide');
      },
      error: function(error) {
        genNotification(error.messageText,'error');
        $('#modalPassageiro').modal('hide');
      }    
    });
  }
});

function modalOpcional(id_passageiro){
  $('#modalOpcional #id_id_passageiro').val(id_passageiro).change();
  $('#modalOpcional').modal('show');
}

$('#new_opcional_btn').on('click', function(event) {
  $('#form-opcional').validate();
  var csrftoken = getCookie('csrftoken');
  if($('#form-opcional').valid()){
    var formData = new FormData($('#form-opcional')[0]);
    formData.append('csrfmiddlewaretoken', csrftoken);
    $.ajax({
      url: url_opcional,
      type: 'POST',
      enctype: "multipart/form-data",
      cache: false,
      contentType: false,
      processData: false,
      data: formData,
      success : function(response) {
        if(response.status == "success"){
        genNotification('Opcional adicionado com sucesso!','success');
        $('#divDetalhes').html(response.html);
        }
        else{
          genNotification(response.message,'error');
        }
        $('#modalOpcional').modal('hide');
      },
      error: function(error) {
        genNotification(error.messageText,'error');
        $('#modalOpcional').modal('hide');
      }    
    });
  }
});


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

})



$(function() {
  $("#id_id_excursao").select2();
  $("#id_id_pacote").select2();
  $("#id_id_passageiro").select2();
  $("#id_id_status_reserva_passageiro").select2();
  $("#id_id_acomodacao_pacote").select2();
})


function setExcursaoPacote(select){
  console.log("setExcursaoPacote")
  var selected = select.options[select.selectedIndex]
  var valor = selected.value
  var id = String(select.id).split('-')[1]
  setPacote(valor,id);
  $("#id_id_pacote").parent().children().find('.select2-choice').find('.select2-chosen').html('---------');
  $('#id_id_pacote').prop('disabled', false);
  $('#id_id_status_reserva option[value="RESERVADO"]').prop('selected', true);
}

function setPacoteAcomodacao(select){
  console.log("setPacoteAcomodacao")
  var selected = select.options[select.selectedIndex]
  var valor = selected.value
  var id = String(select.id).split('-')[1]
  setMoeda(valor,id)
  $("#id_id_acomodacao_pacote").parent().children().find('.select2-choice').find('.select2-chosen').html('---------');
  $('#id_id_acomodacao_pacote').prop('disabled', false);
}


function setPrecoAcomodacao(select){
  console.log("setPrecoAcomodacao")
  var selected = select.options[select.selectedIndex]
  var valor = selected.value
  var id = String(select.id).split('-')[1]
  $('#id_preco_acomodacao').val(selected.getAttribute('data-preco'));
  $('#id_preco_acomodacao').prop('disabled', false);
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
          $("#id_id_pacote").html(htmlString);
        }
      },
      error: function(error) {
        console.log(error);
      }    
    });
  }else{
    htmlString = '<option selected="selected" value="">---------</option>'
    $("#id_id_pacote").parent().children().find('a').find('.select2-chosen').html("---------")
    $("#id_id_pacote").html(htmlString);
    $("#id_id_acomodacao_pacote").parent().children().find('a').find('.select2-chosen').html("---------")
    $("#id_id_acomodacao_pacote").html(htmlString);
    $('#id_reserva_passageiro_preco').val("");
    $('#id_id_moeda').val("");
    $('#id_reserva_passageiro_cambio').val("");
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
          $('#id_reserva_passageiro_preco').val(pacote[0].pacote_preco)
          $("#id_id_moeda").html(htmlString+'<option selected="selected" value="'+pacote[0].id_moeda+'">'+pacote[0].id_moeda__moeda_desc+'</option>');
          $('#id_reserva_passageiro_cambio').val(pacote[0].id_moeda__moeda_cambio)


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
  console.log(select);
  var selected = select.options[select.selectedIndex]
  var id_passageiro = selected.value
  var id = String(select.id).split('-')[1]
  var id_reserva = $('#id_reserva').html()
  setOpcional(id_reserva, id_passageiro);
  $("#id_id_opcional").parent().children().find('.select2-choice').find('.select2-chosen').html('---------');
  $('#id_id_opcional').prop('disabled', false);
}

function setOpcional(id_reserva, id_passageiro){
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
      $("#id_id_opcional").html(htmlString);

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
      $("#id_id_reserva_passageiro").html(htmlString);
      setOpcionals(id_passageiro);
    },

    error: function(error) {
      console.log(error);
    }  

  });
}

function setOpcionals(id_passageiro){
  try{
    var select = document.getElementById('id_id_opcional');
    var passageiro_opcional = $('#passageiro_'+id_passageiro).html().replace(/^\s+|\s+$/g,"");
    passageiro_opcional = passageiro_opcional.split("|");
    for(i=0; i < passageiro_opcional.length; i++){
      for(j=0; j < select.options.length; j++){
        if(passageiro_opcional[i] == select.options[j].value && select.options[j].value){
          select.remove(j);
          break
        }
      }
    }
  }catch(error){
    console.log("No opcionals to set.")
  }
}

function setPassageiroMoedaOpcional(select){
  console.log("setPassageiroMoedaOpcional")
  var selected = select.options[select.selectedIndex]
  var id_opcional = selected.value
  var id = String(select.id).split('-')[1]
  var id_reserva_passageiro = $("#id_id_reserva_passageiro").val()
  
  setMoedaOpcional(id_reserva_passageiro, id_opcional);
}

function setMoedaOpcional(id_reserva_passageiro, id_opcional){
  var url = '/framework/dashboard/passageiro/opcional/passageiro_opcional_moeda_json/' + String(id_reserva_passageiro) + "/" + String(id_opcional);
  $.ajax({
    url: url,
    type: 'GET',

    success : function(response) {
      $("#modalOpcional #id_moeda_desc").val(response.moeda_desc);
      htmlString = '<option value="">---------</option>';
      htmlString += '<option selected="selected" value="'+response.id_moeda+'">'+response.moeda_desc+'</option>';
      $("#modalOpcional #id_id_moeda").html(htmlString);
    },

    error: function(error) {
      console.log(error);
    }  

  });
}