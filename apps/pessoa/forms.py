from .models import * 
from django import forms

class PessoaFisicaForm(forms.ModelForm):
	class Meta:
		model = PessoaFisica
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super(PessoaFisicaForm, self).__init__(*args, **kwargs)
		self.fields['cpf_cnpj'].widget.attrs['class'] = 'form-control'
		self.fields['nome'].widget.attrs['class'] = 'form-control'
		self.fields['email'].widget.attrs['class'] = 'form-control'
		self.fields['data_nascimento'].widget.attrs['class'] = 'form-control'
		self.fields['rg'].widget.attrs['class'] = 'form-control'
		self.fields['orgaoemissor'].widget.attrs['class'] = 'form-control'

		self.fields['data_nascimento'].widget.attrs['placeholder'] = '__/__/__'


class PessoaJuridicaForm(forms.ModelForm):
	class Meta:
		model = PessoaJuridica
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super(PessoaJuridicaForm, self).__init__(*args, **kwargs)
		self.fields['cpf_cnpj'].widget.attrs['class'] = 'form-control'
		self.fields['nome'].widget.attrs['class'] = 'form-control'
		self.fields['email'].widget.attrs['class'] = 'form-control'
		self.fields['razao_social'].widget.attrs['class'] = 'form-control'