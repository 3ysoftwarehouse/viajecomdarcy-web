#-*- coding: utf-8 -*-
from django import forms
from django.conf import settings

from .models import Opcional, Cidade, Excursao


class ExcursaoRegisterForm(forms.ModelForm):

    class Meta:
        model = Excursao
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ExcursaoRegisterForm, self).__init__(*args, **kwargs)
        self.fields['excurcao_desc'].required = True
        self.fields['excurcao_desc'].widget.attrs['class'] = 'form-control'
        self.fields['excurcao_desc'].widget.attrs['placeholder'] = 'Digite a descrição'
        self.fields['is_active'].widget.attrs['class'] = 'form-control'
        self.fields['is_active'].widget.attrs['checked'] = 'checked' 
    		
		


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