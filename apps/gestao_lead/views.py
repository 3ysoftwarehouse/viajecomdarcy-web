from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from apps.default.views import JSONResponseMixin
from django.views.generic import *
from .models import *
from .forms import *


class ProspectRegister(JSONResponseMixin,View):
	def get(self, request):
		form = ProspectForm
		return render (request, 'gestao_lead/prospect/register.html', {'form':form})

	def post(self, request, *args, **kwargs):
		context = {}
		form = ProspectForm(request.POST, request.FILES)		
		if form.is_valid():	    
			prospect = form.save(commit=False)
			prospect.save()
			return redirect(reverse_lazy("prospect-list"))
		context = {'form':form}
		return render(request, 'gestao_lead/prospect/register.html', context)


class ProspectEdit(JSONResponseMixin,View):
	def get(self, request, pk):
		prospect = Prospect.objects.get(pk=pk)
		form = ProspectForm(instance=prospect)
		return render (request, 'gestao_lead/prospect/edit.html', {'form':form})

	def post(self, request, pk, *args, **kwargs):
		context = {}
		prospect = Prospect.objects.get(pk=pk)
		form = ProspectForm(request.POST, request.FILES, instance=prospect)		
		if form.is_valid() :	    
			prospect = form.save(commit=False)
			prospect.save()
			return redirect(reverse_lazy("prospect-list"))
		context = {'form':form}
		return render(request, 'gestao_lead/prospect/edit.html', context)


class ProspectList(JSONResponseMixin,ListView):
	queryset = Prospect.objects.all()
	template_name = 'gestao_lead/prospect/list.html'

	def get_context_data(self, **kwargs):
		context = super(ProspectList, self).get_context_data(**kwargs)
		return context


class ProspectDetail(JSONResponseMixin,DetailView):
	model = Prospect
	template_name = 'gestao_lead/prospect/detail.html'

	def get_context_data(self, **kwargs):
		context = super(ProspectDetail, self).get_context_data(**kwargs)
		return context


class ProspectDelete(JSONResponseMixin,DeleteView):
	model = Prospect
	success_url = reverse_lazy('prospect-list')
	template_name = 'gestao_lead/prospect/delete.html'