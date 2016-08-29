#-*- coding: utf-8 -*-


##################################################
#               DJANGO IMPORTS                   #
##################################################
from django import forms
from django.conf import settings
from django.contrib.admin.widgets import FilteredSelectMultiple
##################################################


##################################################
#               CUSTOM IMPORTS                   #
##################################################
from .models import Pacote # MODELS
from apps.moeda.models import Moeda
from apps.excursao.models import Excursao, Opcional
##################################################

class PacoteRegisterForm(forms.Form):

	id_excursao = forms.ModelChoiceField (queryset=Excursao.objects.all())
	id_moeda = forms.ModelChoiceField (queryset=Moeda.objects.all())
	pacote_nome = forms.CharField(max_length=45)
	pacote_desc = forms.CharField(max_length=200)
	is_active = forms.BooleanField()
	pacote_preco = forms.DecimalField()
	pacote_taxa = forms.DecimalField()
	pacote_daybyday = forms.CharField(max_length=200)
	pacote_obs = forms.CharField(max_length=200)

	id_opcional = forms.ModelMultipleChoiceField(\
      widget=FilteredSelectMultiple("Opcional", is_stacked=False),\
      queryset=Opcional.objects.all())

	def __init__(self, *args, **kwargs):
		super(PacoteRegisterForm, self).__init__(*args, **kwargs)
		# id_excursao Fields widget
		self.fields['id_excursao'].widget.attrs['class'] = 'form-control'

		# id_moeda Fields widget
		self.fields['id_moeda'].widget.attrs['class'] = 'form-control'

		# pacote_nome Fields widget
		self.fields['pacote_nome'].widget.attrs['class'] = 'form-control'

		# pacote_desc Fields widget
		self.fields['pacote_desc'].widget.attrs['class'] = 'form-control'

		# is_active Fields widget
		self.fields['is_active'].widget.attrs['class'] = 'form-control'

		# pacote_preco Fields widget
		self.fields['pacote_preco'].widget.attrs['class'] = 'form-control'

		# pacote_taxa Fields widget
		self.fields['pacote_taxa'].widget.attrs['class'] = 'form-control'

		# pacote_daybyday Fields widget
		self.fields['pacote_daybyday'].widget.attrs['class'] = 'form-control'

		# pacote_obs Fields widget
		self.fields['pacote_obs'].widget.attrs['class'] = 'form-control'

		# id_opcional Fields widget
		self.fields['id_opcional'].widget.attrs['class'] = 'full-width'
		
		pass


	


