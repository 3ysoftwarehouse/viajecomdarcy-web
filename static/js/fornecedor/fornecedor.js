var edit;

if (!edit){

  $("#id_pessoa-fisica-data_nascimento").mask("99/99/9999");
  $("#id_pessoa-juridica-cpf_cnpj").mask("99.999.999/9999-99");
  $("#id_pessoa-fisica-cpf_cnpj").mask("999.999.999-99");

  $('#form_pessoa_juridica').hide();
  $('#check_fisica').click(function(event){
      $('#form_pessoa_juridica').hide();
      $('#form_pessoa_fisica').show();
      $('#fisica').prop('checked', true);
      $('#juridica').prop('checked', false);

  });
  $('#check_juridica').click(function(event){
      $('#form_pessoa_fisica').hide();
      $('#form_pessoa_juridica').show();
      $('#fisica').prop('checked', false);
      $('#juridica').prop('checked', true);
  });

  if ($("#check_fisica").is(":checked")) {
    $('#fisica').prop('checked', true);
    $('#juridica').prop('checked', false);
    $('#form_pessoa_juridica').hide();
    $('#form_pessoa_fisica').show();
  } else {
    console.log('dsadsa');
    $('#fisica').prop('checked', false);
    $('#juridica').prop('checked', true);
    $('#form_pessoa_fisica').hide();
    $('#form_pessoa_juridica').show();
  }

} 
$('#obter_dados').click(function(event){
  get_cnpj_data($("#id_pessoa-juridica-cpf_cnpj").val())
});
var hostname = location.host
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
            document.getElementById("id_pessoa-juridica-razao_social").value = response.nome
            if (response.fantasia){
              document.getElementById("id_pessoa-juridica-nome").value = response.fantasia
            }else{
              document.getElementById("id_pessoa-juridica-nome").value = response.nome
            }
            /*
            document.getElementById("id_pais").value = 'Brazil'
            document.getElementById("id_estado").value = response.uf
            document.getElementById("id_cep").value = response.cep
            document.getElementById("id_cidade").value = response.municipio
            document.getElementById("id_bairro").value = response.bairro
            document.getElementById("id_rua").value = response.logradouro
            document.getElementById("id_numeroed").value = response.numero
            document.getElementById("id_complemento").value = response.complemento
            */
        },
        error: function(response) {
            console.log(response)
        }
      });
   }
};