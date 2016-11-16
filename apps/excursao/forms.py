#-*- coding: utf-8 -*-


##################################################
#               DJANGO IMPORTS                   #
##################################################
from django import forms
from django.conf import settings
##################################################


##################################################
#               CUSTOM IMPORTS                   #
##################################################
from .models import Opcional, Cidade
##################################################

class ExcursaoRegisterForm(forms.Form):

	excurcao_desc = forms.CharField(label='Descrição',max_length=45)
	is_active = forms.BooleanField(label='Ativa')

	def __init__(self, *args, **kwargs):
		super(ExcursaoRegisterForm, self).__init__(*args, **kwargs)
		# excurcao_desc Fields widget
		self.fields['excurcao_desc'].widget.attrs['class'] = 'form-control'
		self.fields['excurcao_desc'].widget.attrs['placeholder'] = 'Digite a descrição'

		# is_active Fields widget
		self.fields['is_active'].widget.attrs['class'] = 'form-control'
		self.fields['is_active'].widget.attrs['checked'] = 'checked' 
		
		pass


class OpcionalForm(forms.ModelForm):

    class Meta:
        model = Opcional
        fields = ('opcional_desc', 'opcional_preco', 'id_moeda', 'taxa_remessa')

    def __init__(self, *args, **kwargs):
        super(OpcionalForm, self).__init__(*args, **kwargs)
       
        # opcional_desc Fields widget
        self.fields['opcional_desc'].widget.attrs['class'] = 'form-control'
        self.fields['opcional_desc'].widget.attrs['placeholder'] = 'Descrição'

        # opcional_preco Fields widget
        self.fields['opcional_preco'].widget.attrs['class'] = 'form-control'
        self.fields['opcional_preco'].widget.attrs['placeholder'] = 'Preço'

        # id_moeda Fields widget
        self.fields['id_moeda'].widget.attrs['class'] = 'form-control'
        self.fields['id_moeda'].widget.attrs['placeholder'] = 'Moeda'

        # taxa_remessa Fields widget
        self.fields['taxa_remessa'].widget.attrs['class'] = 'form-control'
        self.fields['taxa_remessa'].widget.attrs['placeholder'] = 'Taxa'

    pass


class CidadeForm(forms.ModelForm):

    class Meta:
        model = Cidade
        fields = ('cidade',)


    def __init__(self, *args, **kwargs):
        super(CidadeForm, self).__init__(*args, **kwargs)
        # moeda_desc Fields widget
        self.fields['cidade'].widget.attrs['class'] = 'form-control'
        self.fields['cidade'].widget.attrs['placeholder'] = 'Cidade'

        
    pass