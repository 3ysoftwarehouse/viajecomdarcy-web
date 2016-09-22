#-*- coding: utf-8 -*-

##################################################
#				DJANGO IMPORTS                   #
##################################################
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render,redirect
from django.views.generic import CreateView, RedirectView, View, UpdateView, ListView, DetailView, DeleteView
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.http import (HttpResponse,
                         HttpResponseForbidden,
                         HttpResponseBadRequest)
from django.forms import formset_factory
##################################################



##################################################
#				CUSTOM IMPORTS                   #
##################################################
from .models import Reserva, StatusReserva
from .forms import ReservaForm, ReservaPassageiroForm
from apps.default.views import JSONResponseMixin
from apps.subclasses.usuario.emissor.models import Emissor
from apps.excursao.models import Excursao
from apps.pacote.models import Pacote
##################################################

class ReservaRegister(JSONResponseMixin,View):
	def get(self, request):
		formset = formset_factory(ReservaPassageiroForm)
		try:
			emissor = Emissor.objects.get(id_usuario=request.user.id_usuario)
			status_reserva = StatusReserva.objects.get(descricao="RESERVADO")
			form = ReservaForm(
				initial = {
					'id_emissor': emissor.id_emissor,
					'id_agencia':emissor.id_agencia,
					'id_status_reserva': status_reserva.pk,
				}
			)
		except:
			form = ReservaForm()

		
		return render (request, 'venda/reserva/register.html', { 'form':form, 'formset':formset })


class ExcursaoPacoteJson(JSONResponseMixin,View):

    def get(self, request, *args, **kwargs):
        if self.kwargs:
            try:
                pacotes = Pacote.objects.filter(id_excursao=self.kwargs['pk']).values('id_pacote','pacote_nome', 'pacote_preco')
            except:
                pacotes = None
        if pacotes:
            return JsonResponse({'data':list(pacotes)})
        else:
            return JsonResponse({'data':'error'})