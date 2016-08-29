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
from .models import Excursao, Cidade, Opcional # MODELS
from .forms import ExcursaoRegisterForm
from apps.default.views import JSONResponseMixin
##################################################



'''
----------------------------------------
			EXCURSAO METHODS
----------------------------------------
''' 

class ExcursaoRegister(JSONResponseMixin,View):
	def get(self, request):
		form = ExcursaoRegisterForm
		return render (request, 'excursao/excursao/register.html', {'form':form})

	def post(self, request, *args, **kwargs):
		context = {}
		if request.method == 'POST':		    
			form = ExcursaoRegisterForm(request.POST,request.FILES)
			
			excurcao_desc = request.POST['excurcao_desc']
			is_active = request.POST.get('is_active', False)
			
			
			if not excurcao_desc:
				context['error_msg'] = 'excurcao_desc cannot be empty !'
			
			

			if not context:

				excursao = Excursao()
				excursao.excurcao_desc = excurcao_desc
				excursao.is_active = is_active
				excursao.save()
				
				return redirect(reverse_lazy("excursao-list"))

			else:
				form = ExcursaoRegisterForm(request.POST,request.FILES)
				

		return render(request, 'excursao/excursao/register.html', {'form': form, 'formset':formset})


class ExcursaoEdit(JSONResponseMixin,View):
	def get(self, request, pk=None):
		excursao = Excursao.objects.get(pk=pk)
		
		form = ExcursaoRegisterForm(
			initial={
			'excurcao_desc': excursao.excurcao_desc,
			'is_active': excursao.is_active,				
			}
			)
		return render (request, 'excursao/excursao/register.html', {'form':form})

	def post(self, request, pk=None, *args, **kwargs):
		context = {}
		if request.method == 'POST':		    
			form = ExcursaoRegisterForm(request.POST,request.FILES)
			
			excurcao_desc = request.POST['excurcao_desc']
			is_active = request.POST.get('is_active', False)
			
			
			if not excurcao_desc:
				context['error_msg'] = 'excurcao_desc cannot be empty !'
			

			if not context:

				excursao = Excursao.objects.get(pk=pk)
				excursao.excurcao_desc = excurcao_desc
				excursao.is_active = is_active
				excursao.save()
				
				return redirect(reverse_lazy("excursao-list"))

			else:
				form = ExcursaoRegisterForm(request.POST,request.FILES)

		return render (request, 'excursao/excursao/edit.html', {'form':form ,'context':context})



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

'''
----------------------------------------
			END EXCURSAO METHODS
----------------------------------------
'''


'''
----------------------------------------
			CIDADE METHODS
----------------------------------------
'''
class CidadeRegister(JSONResponseMixin,CreateView):
    model = Cidade
    template_name = 'excursao/cidade/register.html'
    fields = [
    'cidade',
    ]
    success_url = reverse_lazy('cidade-list')



class CidadeEdit(JSONResponseMixin,UpdateView):
    model = Cidade
    template_name = 'excursao/cidade/edit.html'
    fields = [
    'cidade',
    ]
    success_url = reverse_lazy('cidade-list')


class CidadeList(JSONResponseMixin,ListView):
	model = Cidade
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
	success_url = reverse_lazy('pacote-list')
	template_name = 'excursao/cidade/delete.html'
'''
----------------------------------------
			END CIDADE METHODS
----------------------------------------
'''

'''
----------------------------------------
			OPCIONAL METHODS
----------------------------------------
'''
class OpcionalRegister(JSONResponseMixin,CreateView):
    model = Opcional
    template_name = 'excursao/opcional/register.html'
    fields = [
    'opcional_desc', 'opcional_preco','id_moeda'
    ]
    success_url = reverse_lazy('opcional-list')



class OpcionalEdit(JSONResponseMixin,UpdateView):
    model = Opcional
    template_name = 'excursao/opcional/edit.html'
    fields = [
    'opcional_desc', 'opcional_preco','id_moeda'
    ]
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
'''
----------------------------------------
			END OPCIONAL METHODS
----------------------------------------
'''