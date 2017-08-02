
var SPMaskBehavior = function (val) {
return val.replace(/\D/g, '').length === 11 ? '(00) 00000-0000' : '(00) 0000-00009';
},
spOptions = {
onKeyPress: function(val, e, field, options) {
    field.mask(SPMaskBehavior.apply({}, arguments), options);
  }
};

$('.telefone').mask(SPMaskBehavior, spOptions);

$("#submit_button").click(function(){
	if($("#id_email").val() || $("#id_telefone").val()){
		$("#form-personal").submit();
	}else{
		var html = '<ul class="errorlist"><li>É obrigatório o preenchimento do campo email ou telefone.</li></ul>';
		$("#email_error").html(html);
		$("#telefone_error").html(html);
	}
});