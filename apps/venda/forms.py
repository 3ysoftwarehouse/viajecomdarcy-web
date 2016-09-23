#-*- coding: utf-8 -*-


##################################################
#               DJANGO IMPORTS                   #
##################################################
from django import forms
##################################################


##################################################
#               CUSTOM IMPORTS                   #
##################################################
from .models import Reserva, ReservaPassageiro
from apps.excursao.models import Excursao
from apps.pacote.models import Pacote
##################################################


class ReservaForm(forms.ModelForm):

    class Meta:
        model = Reserva
        fields = ('id_cliente','id_status_reserva')


    def __init__(self, *args, **kwargs):
        super(ReservaForm, self).__init__(*args, **kwargs)
        # id_cliente Fields widget
        self.fields['id_cliente'].widget.attrs['class'] = 'form-control'
        # id_status_reserva  Fields widget
        self.fields['id_status_reserva'].widget.attrs['class'] = 'form-control'

    pass


class ReservaPassageiroForm(forms.ModelForm):

    id_excursao = forms.ModelChoiceField (queryset=Excursao.objects.all())
    id_pacote = forms.ModelChoiceField (queryset=Pacote.objects.filter(pk=0))
    class Meta:
        model = ReservaPassageiro
        fields = (
            'id_passageiro', 
            'id_status_reserva_passageiro', 
            'reserva_passageiro_preco','reserva_passageiro_cambio',
            'reserva_passageiro_obs',
            )


    def __init__(self, *args, **kwargs):
        super(ReservaPassageiroForm, self).__init__(*args, **kwargs)
        # id_reserva Fields widget
        self.fields['id_excursao'].widget.attrs['class'] = 'form-control form-excursao'
        # id_passageiro Fields widget
        self.fields['id_passageiro'].widget.attrs['class'] = 'form-control'
        # id_pacote Fields widget
        self.fields['id_pacote'].widget.attrs['class'] = 'form-control form-pacote'
        # id_status_reserva_passageiro  Fields widget
        self.fields['id_status_reserva_passageiro'].widget.attrs['class'] = 'form-control'
        # reserva_passageiro_preco Fields widget
        self.fields['reserva_passageiro_preco'].widget.attrs['class'] = 'form-control'
        # reserva_passageiro_cambio  Fields widget
        self.fields['reserva_passageiro_cambio'].widget.attrs['class'] = 'form-control'
        # reserva_passageiro_obs  Fields widget
        self.fields['reserva_passageiro_obs'].widget.attrs['class'] = 'form-control'

    pass