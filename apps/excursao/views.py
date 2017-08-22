#-*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render,redirect
from django.views.generic import CreateView, RedirectView, View, UpdateView, ListView, DetailView, DeleteView
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.http import (HttpResponse,
                         HttpResponseForbidden,
                         HttpResponseBadRequest)
from django.forms import formset_factory

from .models import Excursao, Cidade, Opcional
from .forms import ExcursaoRegisterForm, OpcionalForm, CidadeForm
from apps.default.views import JSONResponseMixin


class ExcursaoRegister(JSONResponseMixin,View):
	def get(self, request):
		form = ExcursaoRegisterForm
		return render (request, 'excursao/excursao/register.html', {'form':form})

	def post(self, request, *args, **kwargs):
		context = {}
		form = ExcursaoRegisterForm(request.POST, request.FILES)		
		if form.is_valid() :	    
			excursao = form.save(commit=False)
			excursao.save()
			return redirect(reverse_lazy("excursao-list"))
		context = {'form':form}
		return render(request, 'excursao/excursao/register.html', context)


class ExcursaoEdit(JSONResponseMixin,View):
	def get(self, request, pk):
		excursao = Excursao.objects.get(pk=pk)
		form = ExcursaoRegisterForm(instance=excursao)
		return render (request, 'excursao/excursao/edit.html', {'form':form})

	def post(self, request, pk, *args, **kwargs):
		context = {}
		excursao = Excursao.objects.get(pk=pk)
		form = ExcursaoRegisterForm(request.POST, request.FILES, instance=excursao)		
		if form.is_valid() :	    
			excursao = form.save(commit=False)
			excursao.save()
			return redirect(reverse_lazy("excursao-list"))
		context = {'form':form}
		return render(request, 'excursao/excursao/edit.html', context)



class ExcursaoList(JSONResponseMixin,ListView):
	queryset = Excursao.objects.all()
	template_name = 'excursao/excursao/list.html'

	def get_context_data(self, **kwargs):
		context = super(ExcursaoList, self).get_context_data(**kwargs)
		return context


class ExcursaoDetail(JSONResponseMixin,DetailView):
	model = Excursao
	template_name = 'excursao/excursao/detail.html'

	def get_context_data(self, **kwargs):
		context = super(ExcursaoDetail, self).get_context_data(**kwargs)
		return context


class ExcursaoDelete(JSONResponseMixin,DeleteView):
	model = Excursao
	success_url = reverse_lazy('excursao-list')
	template_name = 'excursao/excursao/delete.html'



class CidadeRegister(JSONResponseMixin,CreateView):
    model = Cidade
    form_class = CidadeForm
    template_name = 'excursao/cidade/register.html'
    success_url = reverse_lazy('cidade-list')


class CidadeEdit(JSONResponseMixin,UpdateView):
    model = Cidade
    form_class = CidadeForm
    template_name = 'excursao/cidade/edit.html'
    success_url = reverse_lazy('cidade-list')


class CidadeList(JSONResponseMixin,ListView):
	queryset = Cidade.objects.order_by('cidade')
	template_name = 'excursao/cidade/list.html'

	def get_context_data(self, **kwargs):
		context = super(CidadeList, self).get_context_data(**kwargs)
		return context


class CidadeDetail(JSONResponseMixin,DetailView):
	model = Cidade
	template_name = 'excursao/cidade/detail.html'

	def get_context_data(self, **kwargs):
		context = super(CidadeDetail, self).get_context_data(**kwargs)
		return context


class CidadeDelete(JSONResponseMixin,DeleteView):
	model = Cidade
	success_url = reverse_lazy('cidade-list')
	template_name = 'excursao/cidade/delete.html'



class OpcionalRegister(JSONResponseMixin,CreateView):
    model = Opcional
    form_class = OpcionalForm
    template_name = 'excursao/opcional/register.html'    
    success_url = reverse_lazy('opcional-list')



class OpcionalEdit(JSONResponseMixin,UpdateView):
    model = Opcional
    form_class = OpcionalForm
    template_name = 'excursao/opcional/edit.html'
    success_url = reverse_lazy('opcional-list')


class OpcionalList(JSONResponseMixin,ListView):
	model = Opcional
	template_name = 'excursao/opcional/list.html'

	def get_context_data(self, **kwargs):
		context = super(OpcionalList, self).get_context_data(**kwargs)
		return context


class OpcionalDetail(JSONResponseMixin,DetailView):
	model = Opcional
	template_name = 'excursao/opcional/detail.html'

	def get_context_data(self, **kwargs):
		context = super(OpcionalDetail, self).get_context_data(**kwargs)
		return context


class OpcionalDelete(JSONResponseMixin,DeleteView):
	model = Opcional
	success_url = reverse_lazy('opcional-list')
	template_name = 'excursao/opcional/delete.html'
