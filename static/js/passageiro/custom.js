
//Input mask
$("#id_cnpj").mask("99.999.999/9999-99");
$("#id_cep").mask("99.999-999");
$('#id_data_validade_passaporte').mask("99/99/9999");

//Select2
$("select").select2();

$('#adicionar_escola').on('click', function(event) {
  $('#modalEscola').modal('show');
});

$('#new_escola_btn').on('click', function(event) {
  $('#form-escola').validate();
  var csrftoken = getCookie('csrftoken');
  if($('#form-escola').valid()){
    var formData = new FormData(document.getElementById('form-escola'));
    formData.append('csrfmiddlewaretoken', csrftoken);
    $.ajax({
      url: escola_register_url,
      type: 'POST',
      enctype: "multipart/form-data",
      cache: false,
      contentType: false,
      processData: false,
      data: formData,
      success : function(response) {
        if(response.status == "success"){
          genNotification('Escola adicionada com sucesso!','success');
          var option = new Option(response.nomefantasia, response.id_escola);
          option.selected = true;
          $('#id_id_escola').append(option);
          $('#id_id_escola').trigger("change");
        }else{
          genNotification(response.message,'error');
        }
        
        $('#modalEscola').modal('hide');
      },
      error: function(error) {
        genNotification(error.messageText,'error');
        $('#modalEscola').modal('hide');
      }    
    });
  }
});


function genNotification(message,type){
  $('body').pgNotification({
      style: 'bar',
      message: message,
      position: 'top',
      timeout: 2000,
      type: type
  }).show();
}    


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


var hostname = location.host

//Service CNPJ
function get_cnpj_data(value){
   var cnpj = value.replace(/\D/g,'');
   var url = "http://"+hostname+"/framework/service/cnpj/"
   if(cnpj){
      $.ajax({
        type: 'GET',
        url: url,
        data:{'cnpj':cnpj},
        dataType:'json',
        success: function(response) {
            console.log(response)
            document.getElementById("id_razaosocial").value = response.nome
            if (response.fantasia){
              document.getElementById("id_nomefantasia").value = response.fantasia
            }else{
              document.getElementById("id_nomefantasia").value = response.nome
            }
            document.getElementById("id_pais").value = 'Brazil'
            document.getElementById("id_estado").value = response.uf
            document.getElementById("id_cep").value = response.cep
            document.getElementById("id_cidade").value = response.municipio
            document.getElementById("id_bairro").value = response.bairro
            document.getElementById("id_rua").value = response.logradouro
            document.getElementById("id_numeroed").value = response.numero
            document.getElementById("id_complemento").value = response.complemento
        },
        error: function(response) {
            console.log(response)
        }
      });
   }
};

//Service CEP
function get_cep_data(value){
   var cep = value.replace(/\D/g,'');
   var url = "http://"+hostname+"/framework/service/cep/"
   if(cep){
      $.ajax({
        type: 'GET',
        url: url,
        data:{'cep':cep},
        dataType:'json',
        success: function(response) {
            console.log(response)
            document.getElementById("id_estado").value = response.estado
            document.getElementById("id_cidade").value = response.cidade
            document.getElementById("id_bairro").value = response.bairro
            document.getElementById("id_rua").value = response.logradouro
        },
        error: function(response) {
            console.log(response)
        }
      });
   }
};