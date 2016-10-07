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
from apps.acomodacao.models import Acomodacao
from apps.moeda.models import Moeda
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
    id_pacote = forms.ModelChoiceField (queryset=Pacote.objects.all())
    id_acomodacao_pacote = forms.ModelChoiceField (queryset=Acomodacao.objects.all())
    id_moeda = forms.ModelChoiceField (queryset=Moeda.objects.all(), required=False)

    class Meta:
        model = ReservaPassageiro
        fields = (
            'id_passageiro', 
            'id_status_reserva_passageiro',
            'reserva_passageiro_preco','reserva_passageiro_cambio',
            'reserva_passageiro_obs','registro_interno',
            'desconto', 'preco_acomodacao'
            )


    def __init__(self, *args, **kwargs):
        super(ReservaPassageiroForm, self).__init__(*args, **kwargs)
        # id_reserva Fields widget
        self.fields['id_excursao'].widget.attrs['class'] = 'form-control form-excursao'
        self.fields['id_excursao'].widget.attrs['onchange'] = 'setExcursaoPacote(this)'
        # id_passageiro Fields widget
        self.fields['id_passageiro'].widget.attrs['class'] = 'form-control'
        # id_pacote Fields widget
        self.fields['id_pacote'].widget.attrs['class'] = 'form-control form-pacote'
        self.fields['id_pacote'].widget.attrs['onchange'] = 'setPacoteAcomodacao(this)'
        # id_status_reserva_passageiro  Fields widget
        self.fields['id_status_reserva_passageiro'].widget.attrs['class'] = 'form-control'
        # reserva_passageiro_preco Fields widget
        self.fields['reserva_passageiro_preco'].widget.attrs['class'] = 'form-control'
        # reserva_passageiro_cambio  Fields widget
        self.fields['id_moeda'].widget.attrs['class'] = 'form-control form-moeda'
        # reserva_passageiro_cambio  Fields widget
        self.fields['reserva_passageiro_cambio'].widget.attrs['class'] = 'form-control'
        # reserva_passageiro_obs  Fields widget
        self.fields['reserva_passageiro_obs'].widget.attrs['class'] = 'form-control'
        # registro_interno  Fields widget
        self.fields['registro_interno'].widget.attrs['class'] = 'form-control'
        # desconto  Fields widget
        self.fields['desconto'].widget.attrs['class'] = 'form-control'
        # id_acomodacao_pacote  Fields widget
        self.fields['id_acomodacao_pacote'].widget.attrs['class'] = 'form-control form-acomodacao'
        self.fields['id_acomodacao_pacote'].widget.attrs['onchange'] = 'setPrecoAcomodacao(this)'
        # preco_acomodacao  Fields widget
        self.fields['preco_acomodacao'].widget.attrs['class'] = 'form-control form-preco'
    pass