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
from .models import Reserva, StatusReserva, StatusReservaPassageiro
from .forms import ReservaForm, ReservaPassageiroForm
from apps.default.views import JSONResponseMixin
from apps.subclasses.usuario.emissor.models import Emissor
from apps.subclasses.usuario.cliente.models import Cliente
from apps.subclasses.usuario.passageiro.models import Passageiro
from apps.excursao.models import Excursao
from apps.pacote.models import Pacote
##################################################

class ReservaRegister(JSONResponseMixin,View):
	def get(self, request):

		formset = formset_factory(ReservaPassageiroForm,extra=0)
		initial_data = [
			{'id_status_reserva_passageiro': StatusReservaPassageiro.objects.get(descricao="RESERVADO").pk},
		]

		formset = formset(
				initial = initial_data
			)
		
		try:			
			status_reserva = StatusReserva.objects.get(descricao="RESERVADO")
			form = ReservaForm(
				initial = {
					'id_status_reserva': status_reserva.pk,
				}
			)
		except:
			form = ReservaForm()
		
		return render (request, 'venda/reserva/register.html', { 'form':form, 'formset':formset })

	def post(self, request, pk=None, *args, **kwargs):
		formset = formset_factory(ReservaPassageiroForm)
		formset = formset(request.POST)
		form = ReservaForm(request.POST)

		context = {}		
		data = request.POST

		if not data.get('id_cliente', None):
			context['Cliente'] = "não pode ser vazio"
		else:
			id_cliente = Cliente.objects.get(pk=data['id_cliente'])
		if not data.get('id_status_reserva', None):
			context['Status da Reserva'] = "não pode ser vazio"
		else:
			id_status_reserva = StatusReserva.objects.get(pk=data['id_status_reserva'])

		
		print(formset)
				

		return render (request, 'venda/reserva/register.html', { 'form':form, 'formset':formset, 'context':context })


class ReservaList(JSONResponseMixin,ListView):
	model = Reserva
	template_name = 'venda/reserva/list.html'

	def get_context_data(self, **kwargs):
		context = super(ReservaList, self).get_context_data(**kwargs)
		return context 


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


class PacoteMoedaJson(JSONResponseMixin,View):
    def get(self, request, *args, **kwargs):
        if self.kwargs:
            try:
                pacote = Pacote.objects.filter(pk=self.kwargs['pk']).values('id_pacote','pacote_preco', 'id_moeda__moeda_cambio')
            except:
                pacotes = None
        if pacote:
            return JsonResponse({'data':list(pacote)})
        else:
            return JsonResponse({'data':'error'})