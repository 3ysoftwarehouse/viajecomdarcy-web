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
from .models import Pacote, PacoteOpcional, PacoteCidade, PacoteAcomadacao # MODELS
from apps.moeda.models import Moeda
from apps.acomodacao.models import Acomodacao
from apps.excursao.models import Excursao, Opcional, Cidade
from apps.default.views import JSONResponseMixin
from .forms import PacoteRegisterForm, PacoteCidadeRegisterForm, PacoteAcomodacaoRegisterForm # USER FORMS
##################################################


class PacoteRegister(JSONResponseMixin,View):
    def get(self, request):
        form = PacoteRegisterForm
        PacoteCidadeFormSet = formset_factory(PacoteCidadeRegisterForm)      
        cidadeformset = PacoteCidadeFormSet(prefix='cidade')
        PacoteAcomodacaoFormSet = formset_factory(PacoteAcomodacaoRegisterForm)      
        acomodacaoformset = PacoteAcomodacaoFormSet(prefix='acomodacao')

        return render (request, 'pacote/register.html', {'form':form, 'cidadeformset':cidadeformset, 'acomodacaoformset':acomodacaoformset})

    def post(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':            
            form = PacoteRegisterForm(request.POST)

            PacoteCidadeFormSet = formset_factory(PacoteCidadeRegisterForm)      
            cidadeformset = PacoteCidadeFormSet(request.POST, request.FILES, prefix='cidade')
            PacoteAcomodacaoFormSet = formset_factory(PacoteAcomodacaoRegisterForm)      
            acomodacaoformset = PacoteAcomodacaoFormSet(request.POST, request.FILES, prefix='acomodacao')

            id_excursao = request.POST['id_excursao']
            id_moeda = request.POST['id_moeda']
            pacote_nome = request.POST['pacote_nome']
            pacote_desc = request.POST['pacote_desc']
            is_active = request.POST['is_active']
            pacote_preco = request.POST['pacote_preco']
            pacote_taxa = request.POST['pacote_taxa']
            pacote_daybyday = request.POST['pacote_daybyday']
            pacote_obs = request.POST['pacote_obs']
            id_opcional = request.POST.getlist('id_opcional')

            if not id_excursao:
                context['error_msg'] = 'id_excursao cannot be empty !'
            if not id_moeda:
                context['error_msg'] = 'id_moeda cannot be empty !'
            if not pacote_nome:
                context['error_msg'] = 'pacote_nome cannot be empty !'
            if not pacote_desc:
                context['error_msg'] = 'pacote_desc cannot be empty !'
            if not is_active:
                context['error_msg'] = 'is_active cannot be empty !'
            if not pacote_preco:
                context['error_msg'] = 'pacote_preco cannot be empty !'
            if not pacote_taxa:
                context['error_msg'] = 'pacote_taxa cannot be empty !'
            if not pacote_daybyday:
                context['error_msg'] = 'pacote_daybyday cannot be empty !'
            if not pacote_obs:
                context['error_msg'] = 'pacote_obs cannot be empty !'
            if not id_opcional:
                context['error_msg'] = 'id_opcional cannot be empty !'


            listcidades = []

            if cidadeformset.is_valid():
                for f in cidadeformset:
                    cidade = f.cleaned_data
                    listcidades.append([cidade.get('id_cidade'),cidade.get('qtd_dias')])

                    if not cidade.get('id_cidade'):
                        context['Cidade'] = ' cannot be empty !'
                    if not cidade.get('qtd_dias'):
                        context['Dias'] = ' cannot be empty !'
            else:
                for erro in cidadeformset.errors:                 
                    context['error'] = erro
                pass

            listacomodacoes = []

            if acomodacaoformset.is_valid():
                for f in acomodacaoformset:
                    acomodacao = f.cleaned_data
                    listacomodacoes.append([acomodacao.get('id_acomodacao'),acomodacao.get('preco')])

                    '''
                    if not acomodacao.get('id_acomodacao'):
                        context['Acomodação'] = ' cannot be empty !'
                    if not acomodacao.get('preco'):
                        context['Preço'] = ' cannot be empty !'
                    '''
            else:
                for erro in acomodacaoformset.errors:                 
                    context['error'] = erro
                pass

            if not context:
              
                pacote = Pacote()
                pacote.id_excursao = Excursao.objects.get(pk=id_excursao)
                pacote.id_moeda = Moeda.objects.get(pk=id_moeda)
                pacote.pacote_nome = pacote_nome
                pacote.pacote_desc = pacote_desc
                pacote.is_active = is_active
                pacote.pacote_preco = pacote_preco
                pacote.pacote_taxa = pacote_taxa
                pacote.pacote_daybyday = pacote_daybyday
                pacote.pacote_obs = pacote_obs
                pacote.save()

                for value in id_opcional:
                    pacoteopcional = PacoteOpcional()
                    pacoteopcional.id_pacote = Pacote.objects.get(pk=pacote.pk)
                    pacoteopcional.id_opcional = Opcional.objects.get(pk=value)
                    pacoteopcional.save()

                for i, listcidade in enumerate(listcidades):
                    print(listcidade[0])
                    pacotecidade = PacoteCidade()
                    pacotecidade.id_pacote = Pacote.objects.get(pk=pacote.pk)
                    pacotecidade.id_cidade = Cidade.objects.get(cidade=listcidade[0])
                    pacotecidade.qtd_dias = listcidade[1]
                    pacotecidade.ordem = i
                    pacotecidade.save()

                for listacomodacao in listacomodacoes:
                    pacoteacomodacao = PacoteAcomadacao()
                    pacoteacomodacao.id_pacote = Pacote.objects.get(pk=pacote.pk)
                    pacoteacomodacao.id_acomodacao = Acomodacao.objects.get(acomodacao_desc=listacomodacao[0])
                    pacoteacomodacao.id_moeda = Moeda.objects.get(pk=id_moeda)
                    pacoteacomodacao.preco = listacomodacao[1]
                    pacoteacomodacao.save()

                
                return redirect(reverse_lazy('pacote-list'))

            else:
                form = PacoteRegisterForm(request.POST, request.FILES)

                PacoteCidadeFormSet = formset_factory(PacoteCidadeRegisterForm)      
                cidadeformset = PacoteCidadeFormSet(request.POST, request.FILES, prefix='cidade')
                PacoteAcomodacaoFormSet = formset_factory(PacoteAcomodacaoRegisterForm)      
                acomodacaoformset = PacoteAcomodacaoFormSet(request.POST, request.FILES, prefix='acomodacao')


        return render(request, 'pacote/register.html', {'form': form, 'cidadeformset': cidadeformset, 'acomodacaoformset':acomodacaoformset, 'context':context})



class PacoteEdit(JSONResponseMixin,View):
    def get(self, request, pk=None):
        pacote = Pacote.objects.get(pk=pk)
        pacoteopcional = PacoteOpcional.objects.filter(id_pacote=pk)
        pacoteacomodacao = PacoteAcomadacao.objects.filter(id_pacote=pk)
        pacotecidades = PacoteCidade.objects.filter(id_pacote=pk)

        PacoteCidadeFormSet = formset_factory(PacoteCidadeRegisterForm,extra=0)
        PacoteAcomodacaoFormSet = formset_factory(PacoteAcomodacaoRegisterForm, extra=0)   

        opcionais = []
        acomodacoes = []
        cidades = []

        for value in pacoteopcional:
            opcionais.append(value.id_opcional.pk)

       
        for acomodacao in pacoteacomodacao:
            acomodacoes.append({'id_acomodacao':acomodacao.id_acomodacao,'preco':acomodacao.preco})
               
        acomodacaoformset = PacoteAcomodacaoFormSet(
            initial=acomodacoes,
            prefix='acomodacao'
            )

        
        for cidade in pacotecidades:
            cidades.append({'id_cidade':cidade.id_cidade,'qtd_dias':cidade.qtd_dias})
        
                
        cidadeformset = PacoteCidadeFormSet(
            initial=cidades,
            prefix='cidade'
            )

        form = PacoteRegisterForm(
            initial={
            'id_excursao': pacote.id_excursao,
            'id_moeda': pacote.id_moeda,
            'pacote_nome': pacote.pacote_nome,
            'pacote_desc': pacote.pacote_desc,
            'is_active': pacote.is_active,
            'pacote_preco': pacote.pacote_preco,
            'pacote_taxa': pacote.pacote_taxa,
            'pacote_daybyday': pacote.pacote_daybyday,
            'pacote_obs': pacote.pacote_obs,
            }
        )
        return render (request, 'pacote/edit.html', {'form':form, 'opcionais':opcionais,'cidadeformset':cidadeformset, 'acomodacaoformset':acomodacaoformset})

    def post(self, request, pk=None, *args, **kwargs):
        context = {}
        if request.method == 'POST':  

            form = PacoteRegisterForm(request.POST)

            PacoteCidadeFormSet = formset_factory(PacoteCidadeRegisterForm)      
            cidadeformset = PacoteCidadeFormSet(request.POST, request.FILES, prefix='cidade')
            PacoteAcomodacaoFormSet = formset_factory(PacoteAcomodacaoRegisterForm)      
            acomodacaoformset = PacoteAcomodacaoFormSet(request.POST, request.FILES, prefix='acomodacao')

            
            id_excursao = request.POST['id_excursao']
            id_moeda = request.POST['id_moeda']
            pacote_nome = request.POST['pacote_nome']
            pacote_desc = request.POST['pacote_desc']
            is_active = request.POST['is_active']
            pacote_preco = request.POST['pacote_preco']
            pacote_taxa = request.POST['pacote_taxa']
            pacote_daybyday = request.POST['pacote_daybyday']
            pacote_obs = request.POST['pacote_obs']
            id_opcional = request.POST.getlist('id_opcional')

            if not id_excursao:
                context['error_msg'] = 'id_excursao cannot be empty !'
            if not id_moeda:
                context['error_msg'] = 'id_moeda cannot be empty !'
            if not pacote_nome:
                context['error_msg'] = 'pacote_nome cannot be empty !'
            if not pacote_desc:
                context['error_msg'] = 'pacote_desc cannot be empty !'
            if not is_active:
                context['error_msg'] = 'is_active cannot be empty !'
            if not pacote_preco:
                context['error_msg'] = 'pacote_preco cannot be empty !'
            if not pacote_taxa:
                context['error_msg'] = 'pacote_taxa cannot be empty !'
            if not pacote_daybyday:
                context['error_msg'] = 'pacote_daybyday cannot be empty !'
            if not pacote_obs:
                context['error_msg'] = 'pacote_obs cannot be empty !'
            if not id_opcional:
                context['error_msg'] = 'id_opcional cannot be empty !'
            
            listcidades = []

            if cidadeformset.is_valid():
                for f in cidadeformset:
                    cidade = f.cleaned_data
                    listcidades.append([cidade.get('id_cidade'),cidade.get('qtd_dias'),cidade.get('id_pacote_cidade')])

                    if not cidade.get('id_cidade'):
                        context['Cidade'] = ' cannot be empty !'
                    if not cidade.get('qtd_dias'):
                        context['Dias'] = ' cannot be empty !'
            else:
                for erro in cidadeformset.errors:                 
                    context['error'] = erro
                pass


            listacomodacoes = []

            if acomodacaoformset.is_valid():
                for f in acomodacaoformset:
                    acomodacao = f.cleaned_data
                    listacomodacoes.append([acomodacao.get('id_acomodacao'),acomodacao.get('preco')])

                    if not acomodacao.get('id_acomodacao'):
                        context['Acomodação'] = ' cannot be empty !'
                    if not acomodacao.get('preco'):
                        context['Preço'] = ' cannot be empty !'
            else:
                for erro in acomodacaoformset.errors:                 
                    context['error'] = erro
                pass

            if not context:

                
                pacote = Pacote.objects.get(pk=pk)
                pacote.id_excursao = Excursao.objects.get(pk=id_excursao)
                pacote.id_moeda = Moeda.objects.get(pk=id_moeda)
                pacote.pacote_nome = pacote_nome
                pacote.pacote_desc = pacote_desc
                pacote.is_active = is_active
                pacote.pacote_preco = pacote_preco
                pacote.pacote_taxa = pacote_taxa
                pacote.pacote_daybyday = pacote_daybyday
                pacote.pacote_obs = pacote_obs
                pacote.save()

                pacoteopcional = PacoteOpcional.objects.filter(id_pacote=pk)
                pacotecidade = PacoteCidade.objects.filter(id_pacote=pk)
                pacoteacomodacao = PacoteAcomadacao.objects.filter(id_pacote=pk)

                for value in pacoteopcional:
                    value.delete()

                for value in pacotecidade:
                    value.delete()

                for value in pacoteacomodacao:
                    value.delete()


                for value in id_opcional:
                    pacoteopcional = PacoteOpcional()
                    pacoteopcional.id_pacote = Pacote.objects.get(pk=pacote.pk)
                    pacoteopcional.id_opcional = Opcional.objects.get(pk=value)
                    pacoteopcional.save()

                for i, listcidade in enumerate(listcidades):
                    pacotecidade = PacoteCidade()
                    pacotecidade.id_pacote = Pacote.objects.get(pk=pacote.pk)
                    pacotecidade.id_cidade = Cidade.objects.get(cidade=listcidade[0])
                    pacotecidade.qtd_dias = listcidade[1]
                    pacotecidade.ordem = i
                    pacotecidade.save()

                for listacomodacao in listacomodacoes:
                    pacoteacomodacao = PacoteAcomadacao()
                    pacoteacomodacao.id_pacote = Pacote.objects.get(pk=pacote.pk)
                    pacoteacomodacao.id_acomodacao = Acomodacao.objects.get(acomodacao_desc=listacomodacao[0])
                    pacoteacomodacao.id_moeda = Moeda.objects.get(pk=id_moeda)
                    pacoteacomodacao.preco = listacomodacao[1]
                    pacoteacomodacao.save()
                
                return redirect(reverse_lazy('pacote-list'))

            else:
                form = PacoteRegisterForm(request.POST)

                PacoteCidadeFormSet = formset_factory(PacoteCidadeRegisterForm)      
                cidadeformset = PacoteCidadeFormSet(request.POST, request.FILES, prefix='cidade')
                PacoteAcomodacaoFormSet = formset_factory(PacoteAcomodacaoRegisterForm)      
                acomodacaoformset = PacoteAcomodacaoFormSet(request.POST, request.FILES, prefix='acomodacao')


        return render(request, 'pacote/edit.html', {'form': form, 'cidadeformset': cidadeformset, 'acomodacaoformset':acomodacaoformset, 'context':context})



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