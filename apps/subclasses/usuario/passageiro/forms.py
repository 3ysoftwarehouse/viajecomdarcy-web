#-*- coding: utf-8 -*-


##################################################
#               DJANGO IMPORTS                   #
##################################################
from django import forms
from django.conf import settings
from django.contrib.auth.forms import ReadOnlyPasswordHashField
##################################################


##################################################
#               CUSTOM IMPORTS                   #
##################################################
from apps.default.forms import UserRegisterForm
from apps.subclasses.empresa.escola.models import Escola

##################################################

class PassageiroRegisterForm(UserRegisterForm, forms.Form):

	id_escola = forms.ModelChoiceField (queryset = Escola.objects.all())
	matricula = forms.IntegerField(label='Matricula:')
	natularidade = forms.CharField(label='Natularidade:', max_length=30)
	observacao = forms.CharField(label='Obs:', max_length=250)
	