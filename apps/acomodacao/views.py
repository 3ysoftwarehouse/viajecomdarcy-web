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
from .models import Acomodacao # MODELS
from .forms import AcomodacaoForm
from apps.default.views import JSONResponseMixin
##################################################


class AcomodacaoRegister(JSONResponseMixin,CreateView):
    model = Acomodacao
    form_class = AcomodacaoForm
    template_name = 'acomodacao/register.html'
    #fields = ['acomodacao_desc', 'sigla', 'numero']
    success_url = reverse_lazy('acomodacao-list')



class AcomodacaoEdit(JSONResponseMixin,UpdateView):
    model = Acomodacao
    form_class = AcomodacaoForm
    template_name = 'acomodacao/edit.html'
    #fields = ['acomodacao_desc', 'sigla', 'numero']
    success_url = reverse_lazy('acomodacao-list')


class AcomodacaoList(JSONResponseMixin,ListView):
	model = Acomodacao
	template_name = 'acomodacao/list.html'

	def get_context_data(self, **kwargs):
		context = super(AcomodacaoList, self).get_context_data(**kwargs)
		return context


class AcomodacaoDetail(JSONResponseMixin,DetailView):
	model = Acomodacao
	template_name = 'acomodacao/detail.html'

	def get_context_data(self, **kwargs):
		context = super(AcomodacaoDetail, self).get_context_data(**kwargs)
		return context


class AcomodacaoDelete(JSONResponseMixin,DeleteView):
	model = Acomodacao
	success_url = reverse_lazy('acomodacao-list')
	template_name = 'acomodacao/delete.html'