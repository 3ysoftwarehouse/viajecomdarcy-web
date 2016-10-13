$("#id_cnpj_empresa").mask("99.999.999/9999-99"); //CNPJ EMPRESA
$("#id_dt_emissao_rg").mask("99/99/9999"); // DATA
$("#id_dt_admissao").mask("99/99/9999"); // DATA
$("#id_dt_banco").mask("99/99/9999"); // DATA


$(document).ready(function() {
	$(function() {
		$('.delete-row').prepend('<i class="fs-14 pg-minus"></i> ')
		$('.add-row').prepend('<i class="fs-14 pg-plus"></i> ')
		$(".add-row").click(function(){
			$('.delete-row').each(function (index, value) { 
			  	if(typeof ($(this).children().attr('class')) === 'undefined'){
			  		$(this).prepend('<i class="fs-14 pg-minus"></i> ')
			  	}
			  
			});
		});

	});
});


