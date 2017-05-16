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
from datetime import datetime
import json

from .models import Pacote, PacoteOpcional, PacoteCidade, PacoteAcomadacao 
from apps.moeda.models import Moeda
from apps.acomodacao.models import Acomodacao
from apps.excursao.models import Excursao, Opcional, Cidade
from apps.default.views import JSONResponseMixin
from .forms import PacoteRegisterForm, PacoteCidadeRegisterForm, PacoteAcomodacaoRegisterForm, RequiredFormSet



class PacoteRegister(JSONResponseMixin,View):
    def get(self, request):
        form = PacoteRegisterForm
        PacoteCidadeFormSet = formset_factory(PacoteCidadeRegisterForm, formset=RequiredFormSet)      
        cidadeformset = PacoteCidadeFormSet(prefix='cidade',)
        PacoteAcomodacaoFormSet = formset_factory(PacoteAcomodacaoRegisterForm, formset=RequiredFormSet)
        acomodacaoformset = PacoteAcomodacaoFormSet(prefix='acomodacao')
        context = {'form':form, 'cidadeformset':cidadeformset, 'acomodacaoformset':acomodacaoformset}
        return render (request, 'pacote/register.html', context)

    def post(self, request, *args, **kwargs):
        form = PacoteRegisterForm(request.POST, request.FILES)
        PacoteCidadeFormSet = formset_factory(PacoteCidadeRegisterForm, formset=RequiredFormSet)      
        cidadeformset = PacoteCidadeFormSet(request.POST, request.FILES, prefix='cidade')
        PacoteAcomodacaoFormSet = formset_factory(PacoteAcomodacaoRegisterForm, formset=RequiredFormSet)      
        acomodacaoformset = PacoteAcomodacaoFormSet(request.POST, request.FILES, prefix='acomodacao')
        id_opcional = request.POST.getlist('id_opcional')
        try:
            request.POST['data_prevista'] = datetime.strptime(request.POST['data_prevista'], '%d/%m/%Y').strftime('%Y-%m-%d')    
        except:
            pass
        if form.is_valid() and cidadeformset.is_valid() and acomodacaoformset.is_valid():        
            pacote = form.save(commit=False)
            pacote.save()

            for opcional in id_opcional:
                pacoteopcional = PacoteOpcional()
                pacoteopcional.id_pacote = pacote
                pacoteopcional.id_opcional = Opcional.objects.get(pk=opcional)
                pacoteopcional.save()
            
            for i, f  in enumerate(cidadeformset):
                cidade = f.cleaned_data
                pacotecidade = PacoteCidade()
                pacotecidade.id_pacote = pacote
                pacotecidade.id_cidade = cidade.get('id_cidade')
                pacotecidade.qtd_dias = cidade.get('qtd_dias')
                pacotecidade.ordem = i
                pacotecidade.save()

            for i, f  in enumerate(acomodacaoformset):
                acomodacao = f.cleaned_data
                pacoteacomodacao = PacoteAcomadacao()
                pacoteacomodacao.id_pacote = pacote
                pacoteacomodacao.id_acomodacao = acomodacao.get('id_acomodacao')
                pacoteacomodacao.id_moeda = form.cleaned_data.get("id_moeda")
                pacoteacomodacao.preco = acomodacao.get('preco')
                pacoteacomodacao.save()

            return redirect(reverse_lazy('pacote-list'))

        context = {'form':form, 'cidadeformset':cidadeformset, 'acomodacaoformset':acomodacaoformset}
        return render(request, 'pacote/register.html', context)


class PacoteEdit(JSONResponseMixin,View):
    def get(self, request, pk):
        pacote = Pacote.objects.get(pk=pk)
        pacoteopcional = PacoteOpcional.objects.filter(id_pacote=pk)
        pacoteacomodacao = PacoteAcomadacao.objects.filter(id_pacote=pk).extra(select={'id_acomodacao': 'id_acomodacao_id', 'preco':'preco'}).values('id_acomodacao', 'preco')
        pacotecidades = PacoteCidade.objects.filter(id_pacote=pk).extra(select={'id_cidade': 'id_cidade_id', 'qtd_dias':'qtd_dias'}).values('id_cidade', 'qtd_dias')
        extra=1

        form = PacoteRegisterForm(instance=pacote)
        form.initial['id_opcional'] = [value.id_opcional.pk for value in pacoteopcional]

        if pacotecidades:
            extra=0
        PacoteCidadeFormSet = formset_factory(PacoteCidadeRegisterForm, formset=RequiredFormSet,extra=extra)      
        cidadeformset = PacoteCidadeFormSet(prefix='cidade', initial=pacotecidades)
        if pacoteacomodacao:
            extra=0
        PacoteAcomodacaoFormSet = formset_factory(PacoteAcomodacaoRegisterForm, formset=RequiredFormSet, extra=extra)
        acomodacaoformset = PacoteAcomodacaoFormSet(prefix='acomodacao', initial=pacoteacomodacao)

        context = {'form':form, 'cidadeformset':cidadeformset, 'acomodacaoformset':acomodacaoformset}
        return render (request, 'pacote/edit.html', context)

    def post(self, request, pk, *args, **kwargs):

        pacote = Pacote.objects.get(pk=pk)
        pacoteopcional = PacoteOpcional.objects.filter(id_pacote=pk)
        pacoteacomodacao = PacoteAcomadacao.objects.filter(id_pacote=pk)
        pacotecidades = PacoteCidade.objects.filter(id_pacote=pk)
        extra=1
        
        form = PacoteRegisterForm(request.POST, request.FILES,instance=pacote)
        form.initial['id_opcional'] = [value.id_opcional.pk for value in pacoteopcional]

        PacoteCidadeFormSet = formset_factory(PacoteCidadeRegisterForm, formset=RequiredFormSet)      
        cidadeformset = PacoteCidadeFormSet(request.POST, request.FILES, prefix='cidade')
        PacoteAcomodacaoFormSet = formset_factory(PacoteAcomodacaoRegisterForm, formset=RequiredFormSet)      
        acomodacaoformset = PacoteAcomodacaoFormSet(request.POST, request.FILES, prefix='acomodacao')
        id_opcional = request.POST.getlist('id_opcional')
        
        try:
            request.POST['data_prevista'] = datetime.strptime(request.POST['data_prevista'], '%d/%m/%Y').strftime('%Y-%m-%d')    
        except:
            pass
        if form.is_valid() and cidadeformset.is_valid() and acomodacaoformset.is_valid():  

            pacote = form.save(commit=False)
            pacote.save()

            for value in pacoteopcional:
                value.delete()

            for value in pacotecidades:
                value.delete()

            for value in pacoteacomodacao:
                value.delete()

            for opcional in id_opcional:
                pacoteopcional = PacoteOpcional()
                pacoteopcional.id_pacote = pacote
                pacoteopcional.id_opcional = Opcional.objects.get(pk=opcional)
                pacoteopcional.save()
            
            for i, f  in enumerate(cidadeformset):
                cidade = f.cleaned_data
                pacotecidade = PacoteCidade()
                pacotecidade.id_pacote = pacote
                pacotecidade.id_cidade = cidade.get('id_cidade')
                pacotecidade.qtd_dias = cidade.get('qtd_dias')
                pacotecidade.ordem = i
                pacotecidade.save()

            for i, f  in enumerate(acomodacaoformset):
                acomodacao = f.cleaned_data
                pacoteacomodacao = PacoteAcomadacao()
                pacoteacomodacao.id_pacote = pacote
                pacoteacomodacao.id_acomodacao = acomodacao.get('id_acomodacao')
                pacoteacomodacao.id_moeda = form.cleaned_data.get("id_moeda")
                pacoteacomodacao.preco = acomodacao.get('preco')
                pacoteacomodacao.save()

            return redirect(reverse_lazy('pacote-list'))

        context = {'form':form, 'cidadeformset':cidadeformset, 'acomodacaoformset':acomodacaoformset}
        return render(request, 'pacote/edit.html', context)







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
        context['list_opcionais'] = PacoteOpcional.objects.filter(id_pacote=self.kwargs['pk'])
        context['list_cidades'] = PacoteCidade.objects.filter(id_pacote=self.kwargs['pk'])
        context['list_acomodacoes'] = PacoteAcomadacao.objects.filter(id_pacote=self.kwargs['pk'])
        return context


class PacoteDelete(JSONResponseMixin,DeleteView):
	model = Pacote
	success_url = reverse_lazy('pacote-list')
	template_name = 'pacote/delete.html'