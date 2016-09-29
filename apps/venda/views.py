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
from .models import Reserva, StatusReserva, StatusReservaPassageiro, ReservaPassageiro
from .forms import ReservaForm, ReservaPassageiroForm
from apps.default.views import JSONResponseMixin
from apps.subclasses.usuario.emissor.models import Emissor
from apps.subclasses.usuario.cliente.models import Cliente
from apps.subclasses.usuario.passageiro.models import Passageiro
from apps.excursao.models import Excursao
from apps.pacote.models import Pacote
from apps.subclasses.usuario.emissor.views import get_emissor
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

		listPassageiros = []
		if formset.is_valid():
			for f in formset:
				value = f.cleaned_data
				listPassageiros.append([
					value.get('id_passageiro'),
					value.get('id_pacote'),
					value.get('id_status_reserva_passageiro'),
					value.get('reserva_passageiro_preco'),
					value.get('reserva_passageiro_cambio'),
					value.get('reserva_passageiro_obs')
					]
					)

				if not value.get('id_passageiro'):
					context['Passagerio'] = "não pode ser vazio"
				if not value.get('id_pacote'):
					context['Pacote'] = "não pode ser vazio"
				if not value.get('id_status_reserva_passageiro'):
					context['Status da Reserva do Passafeiro'] = "não pode ser vazio"
				if not value.get('reserva_passageiro_preco'):
					context['Preço'] = "não pode ser vazio"
				if not value.get('reserva_passageiro_cambio'):
					context['Cambio'] = "não pode ser vazio"
				if not value.get('reserva_passageiro_obs'):
					context['Obs'] = "não pode ser vazio"
		else:
			for erro in formset.errors:                 
				context['error'] = erro
			pass

		try:
			emissor = Emissor.objects.get(id_usuario=request.user.id_usuario)
		except Emissor.DoesNotExist:
			context['Emissor'] = "não encontrado"

		if not context:

			reserva = Reserva()
			reserva.id_cliente = id_cliente
			reserva.id_emissor = emissor
			reserva.id_agencia = emissor.id_agencia
			reserva.id_status_reserva = id_status_reserva
			reserva.save()

			for value in listPassageiros:

				reservapassageiro = ReservaPassageiro() 
				reservapassageiro.id_reserva =  reserva
				reservapassageiro.id_passageiro = value[0]
				reservapassageiro.id_pacote = value[1]
				reservapassageiro.id_status_reserva_passageiro = value[2]
				reservapassageiro.id_escola = value[0].id_escola
				reservapassageiro.reserva_passageiro_preco = value[3]
				reservapassageiro.id_moeda = value[1].id_moeda
				reservapassageiro.reserva_passageiro_cambio = value[4]
				reservapassageiro.reserva_passageiro_obs = value[5]
				reservapassageiro.save()

			return redirect(reverse_lazy('reserva-list'))

		return render (request, 'venda/reserva/register.html', { 'form':form, 'formset':formset, 'context':context })


class ReservaEdit(JSONResponseMixin,View):
	def get(self, request, **kwargs):

		reserva = Reserva.objects.get(pk=self.kwargs['pk'])
		reservapassageiros = ReservaPassageiro.objects.filter(id_reserva=reserva.pk)

		formset = formset_factory(ReservaPassageiroForm,extra=0)
		initial_data = []
		for reservapassageiro in reservapassageiros:
			initial_data.append({
					'id_excursao':reservapassageiro.id_pacote.id_excursao,
					'id_passageiro':reservapassageiro.id_passageiro,
					'id_pacote':reservapassageiro.id_pacote,
					'id_status_reserva_passageiro':reservapassageiro.id_status_reserva_passageiro,
					'reserva_passageiro_preco':reservapassageiro.reserva_passageiro_preco,
					'reserva_passageiro_cambio':reservapassageiro.reserva_passageiro_cambio,
					'reserva_passageiro_obs':reservapassageiro.reserva_passageiro_obs,
				})
			
		

		formset = formset(
				initial = initial_data
			)
		try:			
			form = ReservaForm(
				initial = {
					'id_cliente' : reserva.id_cliente,
					'id_status_reserva': reserva.id_status_reserva,
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

		listPassageiros = []
		if formset.is_valid():
			for f in formset:
				value = f.cleaned_data
				listPassageiros.append([
					value.get('id_passageiro'),
					value.get('id_pacote'),
					value.get('id_status_reserva_passageiro'),
					value.get('reserva_passageiro_preco'),
					value.get('reserva_passageiro_cambio'),
					value.get('reserva_passageiro_obs')
					]
					)

				if not value.get('id_passageiro'):
					context['Passagerio'] = "não pode ser vazio"
				if not value.get('id_pacote'):
					context['Pacote'] = "não pode ser vazio"
				if not value.get('id_status_reserva_passageiro'):
					context['Status da Reserva do Passafeiro'] = "não pode ser vazio"
				if not value.get('reserva_passageiro_preco'):
					context['Preço'] = "não pode ser vazio"
				if not value.get('reserva_passageiro_cambio'):
					context['Cambio'] = "não pode ser vazio"
				if not value.get('reserva_passageiro_obs'):
					context['Obs'] = "não pode ser vazio"
		else:
			for erro in formset.errors:                 
				context['error'] = erro
			pass

		try:
			emissor = Emissor.objects.get(id_usuario=request.user.id_usuario)
		except Emissor.DoesNotExist:
			context['Emissor'] = "não encontrado"

		if not context:

			reserva = Reserva.objects.get(pk=self.kwargs['pk'])
			reservapassageiros = ReservaPassageiro.objects.filter(id_reserva=reserva.pk)

			for value in reservapassageiros:
				value.delete()

			reserva.id_cliente = id_cliente
			reserva.id_emissor = emissor
			reserva.id_agencia = emissor.id_agencia
			reserva.id_status_reserva = id_status_reserva
			reserva.save()

			for value in listPassageiros:

				reservapassageiro = ReservaPassageiro() 
				reservapassageiro.id_reserva =  reserva
				reservapassageiro.id_passageiro = value[0]
				reservapassageiro.id_pacote = value[1]
				reservapassageiro.id_status_reserva_passageiro = value[2]
				reservapassageiro.id_escola = value[0].id_escola
				reservapassageiro.reserva_passageiro_preco = value[3]
				reservapassageiro.id_moeda = value[1].id_moeda
				reservapassageiro.reserva_passageiro_cambio = value[4]
				reservapassageiro.reserva_passageiro_obs = value[5]
				reservapassageiro.save()

			return redirect(reverse_lazy('reserva-list'))

		return render (request, 'venda/reserva/edit.html', { 'form':form, 'formset':formset, 'context':context })

class ReservaList(JSONResponseMixin,ListView):
	template_name = 'venda/reserva/list.html'

	def get_queryset(self):
		emissor = get_emissor(self)
		if emissor:
			return Reserva.objects.filter(id_agencia=emissor.id_agencia.pk)
		else:
			return Reserva.objects.all()

	def get_context_data(self, **kwargs):
		context = super(ReservaList, self).get_context_data(**kwargs)
		return context

class ReservaDetail(JSONResponseMixin,DetailView):
	model = Reserva
	template_name = 'venda/reserva/detail.html'

	def get_context_data(self, **kwargs):
		context = super(ReservaDetail, self).get_context_data(**kwargs)
		return context

class ReservaDelete(JSONResponseMixin,DeleteView):
	model = Reserva
	success_url = reverse_lazy('reserva-list')
	template_name = 'venda/reserva/delete.html' 

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