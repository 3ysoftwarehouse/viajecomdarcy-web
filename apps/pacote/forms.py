#-*- coding: utf-8 -*-
from django import forms
from django.forms import BaseFormSet
from django.conf import settings
from django.contrib.admin.widgets import FilteredSelectMultiple

from .models import Pacote 
from apps.moeda.models import Moeda
from apps.excursao.models import Excursao, Opcional, Cidade
from apps.acomodacao.models import Acomodacao


class RequiredFormSet(BaseFormSet):
	def __init__(self, *args, **kwargs):
		super(RequiredFormSet, self).__init__(*args, **kwargs)
		for form in self.forms:
			form.empty_permitted = False

class PacoteCidadeRegisterForm(forms.Form):
	id_cidade = forms.ModelChoiceField (queryset=Cidade.objects.all(), required=True)
	qtd_dias = forms.IntegerField(min_value=0, required=True)

	def __init__(self, *args, **kwargs):
		super(PacoteCidadeRegisterForm, self).__init__(*args, **kwargs)
		self.fields['id_cidade'].widget.attrs['class'] = 'form-control'
		self.fields['qtd_dias'].widget.attrs['class'] = 'form-control'

		self.fields['id_cidade'].label = "Cidade"
		self.fields['qtd_dias'].label = "Quantidade de dias"


class PacoteRegisterForm(forms.ModelForm):
	id_opcional = forms.ModelMultipleChoiceField(queryset=Opcional.objects.all(), required=False)
	class Meta:
		model = Pacote
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super(PacoteRegisterForm, self).__init__(*args, **kwargs)
		self.fields['id_excursao'].widget.attrs['class'] = 'form-control'
		self.fields['id_moeda'].widget.attrs['class'] = 'form-control'
		self.fields['pacote_nome'].widget.attrs['class'] = 'form-control'
		self.fields['pacote_desc'].widget.attrs['class'] = 'form-control'
		self.fields['is_active'].widget.attrs['class'] = 'form-control'
		self.fields['pacote_preco'].widget.attrs['class'] = 'form-control input-number'
		self.fields['pacote_taxa'].widget.attrs['class'] = 'form-control input-number'
		self.fields['taxa_remessa'].widget.attrs['class'] = 'form-control input-number'
		self.fields['pacote_daybyday'].widget.attrs['class'] = 'form-control'
		self.fields['pacote_obs'].widget.attrs['class'] = 'form-control'
		self.fields['pacote_daybyday'].required = False
		self.fields['pacote_obs'].required = False
		self.fields['id_opcional'].required = False
		self.fields['id_opcional'].widget.attrs['style'] = 'width:100%;'
		self.fields['data_prevista'].widget.attrs['class'] = 'form-control'
		self.fields['data_prevista'].widget.attrs['placeholder'] = '__/__/__'
		self.fields['data_prevista'].required = True

		self.fields['pacote_nome'].label = "Nome do Pacote"
		self.fields['pacote_desc'].label = "Descrição do Pacote"
		self.fields['pacote_preco'].label = "Preço do Pacote"
		self.fields['pacote_taxa'].label = "Taxa do Pacote"
		self.fields['taxa_remessa'].label = "Taxa de Remessa"
		self.fields['pacote_obs'].label = "Observação"
		self.fields['pacote_daybyday'].label = "Day by day"
		self.fields['id_opcional'].label = "Pacote Opcional"
		self.fields['id_excursao'].label = "Excursão"
		self.fields['id_moeda'].label = "Moeda"


class PacoteAcomodacaoRegisterForm(forms.Form):
	id_acomodacao = forms.ModelChoiceField (queryset=Acomodacao.objects.all())
	preco = forms.DecimalField()
	
	def __init__(self, *args, **kwargs):
		super(PacoteAcomodacaoRegisterForm, self).__init__(*args, **kwargs)
		self.fields['id_acomodacao'].widget.attrs['class'] = 'form-control select acomodacao'
		self.fields['preco'].widget.attrs['class'] = 'form-control'

		self.fields['id_acomodacao'].label = "Acomodação"

