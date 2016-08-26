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
from .models import Moeda # MODELS
from apps.default.views import JSONResponseMixin
##################################################


class MoedaRegister(JSONResponseMixin,CreateView):
    model = Moeda
    template_name = 'moeda/register.html'
    fields = ['moeda_desc', 'moeda_cambio', 'moeda_simbolo']
    success_url = reverse_lazy('moeda-list')



class MoedaEdit(JSONResponseMixin,UpdateView):
    model = Moeda
    template_name = 'moeda/edit.html'
    fields = ['moeda_desc', 'moeda_cambio', 'moeda_simbolo']
    success_url = reverse_lazy('moeda-list')


class MoedaList(JSONResponseMixin,ListView):
	model = Moeda
	template_name = 'moeda/list.html'

	def get_context_data(self, **kwargs):
		context = super(MoedaList, self).get_context_data(**kwargs)
		return context


class MoedaDetail(JSONResponseMixin,DetailView):
	model = Moeda
	template_name = 'moeda/detail.html'

	def get_context_data(self, **kwargs):
		context = super(MoedaDetail, self).get_context_data(**kwargs)
		return context


class MoedaDelete(JSONResponseMixin,DeleteView):
	model = Moeda
	success_url = reverse_lazy('moeda-list')
	template_name = 'moeda/delete.html'