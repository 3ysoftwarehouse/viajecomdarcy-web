#-*- coding: utf-8 -*-

##################################################
#				DJANGO IMPORTS                   #
##################################################
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render,redirect
from django.views.generic import RedirectView, View, UpdateView, ListView, DetailView, DeleteView
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
from .models import Excursao # MODELS
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
		return render (request, 'excursao/register.html', {'form':form})

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
				

		return render(request, 'excursao/register.html', {'form': form, 'formset':formset})


class ExcursaoEdit(JSONResponseMixin,View):
	def get(self, request, pk=None):
		excursao = Excursao.objects.get(pk=pk)
		
		form = ExcursaoRegisterForm(
			initial={
			'excurcao_desc': excursao.excurcao_desc,
			'is_active': excursao.is_active,				
			}
			)
		return render (request, 'excursao/register.html', {'form':form})

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

		return render (request, 'excursao/edit.html', {'form':form ,'context':context})



class ExcursaoList(JSONResponseMixin,ListView):
	queryset = Excursao.objects.all()
	template_name = 'excursao/list.html'

	def get_context_data(self, **kwargs):
		context = super(ExcursaoList, self).get_context_data(**kwargs)
		return context


class ExcursaoDetail(JSONResponseMixin,DetailView):
	model = Excursao
	template_name = 'excursao/detail.html'

	def get_context_data(self, **kwargs):
		context = super(ExcursaoDetail, self).get_context_data(**kwargs)
		return context


class ExcursaoDelete(JSONResponseMixin,DeleteView):
	model = Excursao
	success_url = reverse_lazy('excursao-list')
	template_name = 'excursao/delete.html'

'''
----------------------------------------
			END EXCURSAO METHODS
----------------------------------------
'''