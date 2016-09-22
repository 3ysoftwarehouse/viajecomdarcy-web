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
        fields = ('id_cliente', 'id_emissor', 'id_agencia', 'id_status_reserva')


    def __init__(self, *args, **kwargs):
        super(ReservaForm, self).__init__(*args, **kwargs)
        # id_cliente Fields widget
        self.fields['id_cliente'].widget.attrs['class'] = 'form-control'
        # id_emissor Fields widget
        self.fields['id_emissor'].widget.attrs['class'] = 'form-control'
        self.fields['id_emissor'].widget.attrs['disabled'] = 'disabled'
        # id_agencia Fields widget
        self.fields['id_agencia'].widget.attrs['class'] = 'form-control'
        self.fields['id_agencia'].widget.attrs['disabled'] = 'disabled'
        # id_status_reserva  Fields widget
        self.fields['id_status_reserva'].widget.attrs['class'] = 'form-control'

    pass


class ReservaPassageiroForm(forms.ModelForm):

    id_excursao = forms.ModelChoiceField (queryset=Excursao.objects.all())
    id_pacote = forms.ModelChoiceField (queryset=Pacote.objects.filter(pk=0))
    class Meta:
        model = ReservaPassageiro
        fields = (
            'id_reserva', 'id_passageiro', 
            'id_status_reserva_passageiro', 'id_escola', 
            'reserva_passageiro_preco','id_moeda','reserva_passageiro_cambio',
            'reserva_passageiro_obs',
            )


    def __init__(self, *args, **kwargs):
        super(ReservaPassageiroForm, self).__init__(*args, **kwargs)
        # id_reserva Fields widget
        self.fields['id_excursao'].widget.attrs['class'] = 'form-control form-excursao'
        # id_reserva Fields widget
        self.fields['id_reserva'].widget.attrs['class'] = 'form-control'
        # id_passageiro Fields widget
        self.fields['id_passageiro'].widget.attrs['class'] = 'form-control'
        # id_pacote Fields widget
        self.fields['id_pacote'].widget.attrs['class'] = 'form-control'
        # id_status_reserva_passageiro  Fields widget
        self.fields['id_status_reserva_passageiro'].widget.attrs['class'] = 'form-control'
        # id_escola Fields widget
        self.fields['id_escola'].widget.attrs['class'] = 'form-control'
        # reserva_passageiro_preco Fields widget
        self.fields['reserva_passageiro_preco'].widget.attrs['class'] = 'form-control'
        # id_moeda Fields widget
        self.fields['id_moeda'].widget.attrs['class'] = 'form-control'
        # reserva_passageiro_cambio  Fields widget
        self.fields['reserva_passageiro_cambio'].widget.attrs['class'] = 'form-control'
        # reserva_passageiro_obs  Fields widget
        self.fields['reserva_passageiro_obs'].widget.attrs['class'] = 'form-control'

    pass