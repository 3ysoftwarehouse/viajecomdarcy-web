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
from .models import Pacote # MODELS
from apps.default.views import JSONResponseMixin
##################################################


class PacoteRegister(JSONResponseMixin,CreateView):
    model = Pacote
    template_name = 'pacote/register.html'
    fields = [
    'id_excursao', 'id_moeda', 'pacote_nome', 'pacote_desc', 'is_active',
    'pacote_preco', 'pacote_taxa', 'pacote_daybyday', 'pacote_obs'
    ]
    success_url = reverse_lazy('pacote-list')



class PacoteEdit(JSONResponseMixin,UpdateView):
    model = Pacote
    template_name = 'pacote/edit.html'
    fields = [
    'id_excursao', 'id_moeda', 'pacote_nome', 'pacote_desc', 'is_active',
    'pacote_preco', 'pacote_taxa', 'pacote_daybyday', 'pacote_obs'
    ]
    success_url = reverse_lazy('pacote-list')


class PacoteList(JSONResponseMixin,ListView):
	model = Pacote
	template_name = 'pacote/list.html'

	def get_context_data(self, **kwargs):
		context = super(PacoteList, self).get_context_data(**kwargs)
		return context


class PacoteDetail(JSONResponseMixin,DetailView):
	model = Pacote
	template_name = 'pacote/detail.html'

	def get_context_data(self, **kwargs):
		context = super(PacoteDetail, self).get_context_data(**kwargs)
		return context


class PacoteDelete(JSONResponseMixin,DeleteView):
	model = Pacote
	success_url = reverse_lazy('pacote-list')
	template_name = 'pacote/delete.html'