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
from apps.default.models import Projeto, Usuario, Empresa, Logradouro, Endereco, TipoEmpresa, TipoTelefone, TelefoneEmpresa # MODELS
from .forms import EscolaRegisterForm
from apps.default.forms import PhoneForm # PHONE FORMS
from apps.default.views import JSONResponseMixin, validaCNPJ
from .models import Escola
##################################################


'''
----------------------------------------
			ESCOLA METHODS
----------------------------------------
''' 


class EscolaRegister(JSONResponseMixin,View):
	def get(self, request):
		form = EscolaRegisterForm
		formset = formset_factory(PhoneForm)
		return render (request, 'subclasses/empresa/escola/register.html', {'form':form,'formset':formset})

	def post(self, request, *args, **kwargs):
		context = {}
		if request.method == 'POST':

			PhoneFormSet = formset_factory(PhoneForm)		
			formset = PhoneFormSet(request.POST, request.FILES)
			form = EscolaRegisterForm(request.POST, request.FILES)
	
			razaosocial = request.POST['razaosocial']
			nomefantasia = request.POST['nomefantasia']
			cnpj = request.POST['cnpj']
			ie = request.POST['ie']
			id_tipo_empresa = request.POST['tipo_empresa']

			cep = request.POST['cep']
			rua = request.POST['rua']
			bairro = request.POST['bairro']
			cidade = request.POST['cidade']
			estado = request.POST['estado']
			pais = request.POST['pais']

			numeroed = request.POST['numeroed']
			complemento = request.POST['complemento']
			pontoreferencia = request.POST['pontoreferencia']

			'''
			tipo_telefone = request.POST['tipo_telefone']
			numero = request.POST['numero']
			ramal = request.POST['ramal']
			nome_contato = request.POST['nome_contato']
			'''	

			# EXTRAS
			

			if not razaosocial:
				context['Razão social'] = ' cannot be empty !'
			if not nomefantasia:
				context['Nome Fantasia'] = ' cannot be empty !'
			
			if validaCNPJ(cnpj):
				context['CNPJ'] = ' vazio ou ja existente !'		
				
			if not ie:
				context['IE'] = ' cannot be empty !'
			if not id_tipo_empresa:
				context['Tipo de Empresa'] = ' cannot be empty !'
			
			'''
			if not foto:
				context['error_msg'] = 'foto cannot be empty !'
			'''

			if not cep:
				context['CEP'] = ' cannot be empty !'
			if not rua:
				context['Rua'] = ' cannot be empty !'
			if not bairro:
				context['Bairro'] = ' cannot be empty !'
			if not cidade:
				context['Cidade'] = ' cannot be empty !'
			if not estado:
				context['Estado'] = ' cannot be empty !'
			if not pais:
				context['Pais'] = ' cannot be empty !'
			if not numeroed:
				context['Número'] = ' cannot be empty !'
			if not complemento:
				context['Comlemento'] = ' cannot be empty !'

			# EXTRAS
			
			
			listphones = []

			if formset.is_valid():
				for f in formset:
					phone = f.cleaned_data
					listphones.append([phone.get('tipo_telefone'),phone.get('numero'),phone.get('ramal'),phone.get('nome_contato')])

					if not phone.get('tipo_telefone'):
						context['Tipo Telefone'] = ' cannot be empty !'
					if not phone.get('numero'):
						context['Numero'] = ' cannot be empty !'
					if not phone.get('ramal'):
						context['Ramal'] = ' cannot be empty !'
					if not phone.get('nome_contato'):
						context['Contato'] = ' cannot be empty !'
						pass
			else:
				for erro in formset.errors:					
					context['error'] = erro
				pass

		
			if not context:

				id_logradouro = Logradouro()
				id_logradouro.cep = cep
				id_logradouro.bairro = bairro
				id_logradouro.cidade = cidade
				id_logradouro.estado = estado
				id_logradouro.pais = pais
				id_logradouro.nome = rua
				id_logradouro.save()

				id_endereco = Endereco()
				id_endereco.id_logradouro = id_logradouro
				id_endereco.numero = numeroed
				id_endereco.complemento = complemento
				id_endereco.pontoreferencia = pontoreferencia
				id_endereco.save()

				id_tipo_empresa = TipoEmpresa.objects.get(pk=id_tipo_empresa)

				empresa = Empresa()
				empresa.razaosocial = razaosocial
				empresa.nomefantasia = nomefantasia 
				empresa.cnpj = cnpj
				empresa.verificada = True
				empresa.ie = ie
				empresa.id_tipo_empresa = id_tipo_empresa				
				empresa.id_endereco = id_endereco
				empresa.save()

				for listphone in listphones:
					id_tipo_telefone = TipoTelefone.objects.filter(descricao=listphone[0])[0]			
					telempresa = TelefoneEmpresa()
					telempresa.id_tipo_telefone = id_tipo_telefone
					telempresa.id_empresa = empresa
					telempresa.numero = listphone[1]
					telempresa.ramal = listphone[2]
					telempresa.nome_contato = listphone[3]
					telempresa.save()

				# EXTRAS
				escola = Escola()
				escola.id_empresa = empresa
				escola.save()
					
				return redirect(reverse_lazy("escola-list"))

		else:
			PhoneFormSet = formset_factory(PhoneForm)		
			formset = PhoneFormSet(request.POST, request.FILES)
			form = EscolaRegisterForm(request.POST, request.FILES)

		return render(request, 'subclasses/empresa/escola/register.html', {'form': form, 'formset':formset ,'context':context})


class EscolaEdit(JSONResponseMixin,View):
	def get(self, request, pk=None):
		escola = Escola.objects.get(pk=pk)
		empresa = Empresa.objects.get(pk=escola.id_empresa.pk)
		telefones = TelefoneEmpresa.objects.filter(id_empresa=empresa.pk)

		
		PhoneFormSet = formset_factory(PhoneForm,extra=0)
		

		data = []
		for telefone in telefones:
			data.append({'tipo_telefone':telefone.id_tipo_telefone,'numero':telefone.numero,'ramal':telefone.ramal,'nome_contato':telefone.nome_contato})
		
				
		formset = PhoneFormSet(
			initial=data
			)

		form = EscolaRegisterForm(
			initial={
			'razaosocial': escola.id_empresa.razaosocial,
			'nomefantasia': escola.id_empresa.nomefantasia,
			'cnpj': escola.id_empresa.cnpj,
			'verificada': escola.id_empresa.verificada,
			'ie': escola.id_empresa.ie,
			'tipo_empresa': escola.id_empresa.id_tipo_empresa,
			'cep' :  escola.id_empresa.id_endereco.id_logradouro.cep,
		    'rua' :  escola.id_empresa.id_endereco.id_logradouro.nome,
		    'bairro' :  escola.id_empresa.id_endereco.id_logradouro.bairro,
		    'cidade' :  escola.id_empresa.id_endereco.id_logradouro.cidade,
		    'estado' :  escola.id_empresa.id_endereco.id_logradouro.estado,
		    'pais' : escola.id_empresa.id_endereco.id_logradouro.pais,
		    'numeroed' :  escola.id_empresa.id_endereco.numero,
		    'complemento' : escola.id_empresa.id_endereco.complemento,
		    'pontoreferencia' :  escola.id_empresa.id_endereco.pontoreferencia,
		    
			# EXTRAS		    
			}
			)

		return render (request, 'subclasses/empresa/escola/edit.html', {'form':form ,'formset':  formset})

	def post(self, request, pk=None, *args, **kwargs):
		context = {}
		if request.method == 'POST':		    
			form = EscolaRegisterForm(request.POST, request.FILES)
			PhoneFormSet = formset_factory(PhoneForm)		
			formset = PhoneFormSet(request.POST, request.FILES)	  

					  
			
			razaosocial = request.POST['razaosocial']
			nomefantasia = request.POST['nomefantasia']
			cnpj = request.POST['cnpj']
			ie = request.POST['ie']
			id_tipo_empresa = request.POST['tipo_empresa']


			cep = request.POST['cep']
			rua = request.POST['rua']
			bairro = request.POST['bairro']
			cidade = request.POST['cidade']
			estado = request.POST['estado']
			pais = request.POST['pais']

			numeroed = request.POST['numeroed']
			complemento = request.POST['complemento']
			pontoreferencia = request.POST['pontoreferencia']

			
			# EXTRAS
			

			listphones = []

			if formset.is_valid():
				for f in formset:
					phone = f.cleaned_data
					listphones.append([phone.get('tipo_telefone'),phone.get('numero'),phone.get('ramal'),phone.get('nome_contato')])

					if not phone.get('tipo_telefone'):
						context['Tipo Telefone'] = ' cannot be empty !'
					if not phone.get('numero'):
						context['Numero'] = ' cannot be empty !'
					if not phone.get('ramal'):
						context['Ramal'] = ' cannot be empty !'
					if not phone.get('nome_contato'):
						context['Contato'] = ' cannot be empty !'
						pass
			else:
				for erro in formset.errors:					
					context['error'] = erro
				pass
								
			if not razaosocial:
				context['Razão social'] = ' cannot be empty !'
			if not nomefantasia:
				context['Nome Fantasia'] = ' cannot be empty !'
			if not cnpj or not validaCNPJ(cnpj):
				context['CNPJ'] = ' cannot be empty !'			
			if not ie:
				context['IE'] = ' cannot be empty !'
			if not id_tipo_empresa:
				context['Tipo de Empresa'] = ' cannot be empty !'
			
			'''
			if not foto:
				context['error_msg'] = 'foto cannot be empty !'
			'''

			if not cep:
				context['CEP'] = ' cannot be empty !'
			if not rua:
				context['Rua'] = ' cannot be empty !'
			if not bairro:
				context['Bairro'] = ' cannot be empty !'
			if not cidade:
				context['Cidade'] = ' cannot be empty !'
			if not estado:
				context['Estado'] = ' cannot be empty !'
			if not pais:
				context['Pais'] = ' cannot be empty !'
			if not numeroed:
				context['Número'] = ' cannot be empty !'
			if not complemento:
				context['Comlemento'] = ' cannot be empty !'
			if not pontoreferencia:
				context['Ponto de refêrencia'] = ' cannot be empty !'

			# EXTRAS
			

			if not context:

				escola = Escola.objects.get(pk=pk)

				empresa = Empresa.objects.get(pk=escola.id_empresa.pk)
				telefones = TelefoneEmpresa.objects.filter(id_empresa=empresa.pk)
				id_endereco = Endereco.objects.get(id_endereco=empresa.id_endereco.pk)
				id_logradouro = Logradouro.objects.get(id_logradouro=id_endereco.id_logradouro.pk)

				for telefone in telefones:
					telefone.delete()

				id_logradouro = Logradouro()
				id_logradouro.cep = cep
				id_logradouro.bairro = bairro
				id_logradouro.cidade = cidade
				id_logradouro.estado = estado
				id_logradouro.pais = pais
				id_logradouro.nome = rua
				id_logradouro.save()

				
				id_endereco.id_logradouro = id_logradouro
				id_endereco.numero = numeroed
				id_endereco.complemento = complemento
				id_endereco.pontoreferencia = pontoreferencia
				id_endereco.save()

				id_tipo_empresa = TipoEmpresa.objects.get(pk=id_tipo_empresa)
				
				empresa.razaosocial = razaosocial
				empresa.nomefantasia = nomefantasia 
				empresa.cnpj = cnpj
				empresa.verificada = True
				empresa.ie = ie
				empresa.id_tipo_empresa = id_tipo_empresa				
				empresa.id_endereco = id_endereco
				empresa.save()

				
				for listphone in listphones:
					id_tipo_telefone = TipoTelefone.objects.filter(descricao=listphone[0])[0]			
					telempresa = TelefoneEmpresa()
					telempresa.id_tipo_telefone = id_tipo_telefone
					telempresa.id_empresa = empresa
					telempresa.numero = listphone[1]
					telempresa.ramal = listphone[2]
					telempresa.nome_contato = listphone[3]
					telempresa.save()

				# EXTRAS
				escola.id_empresa = empresa
				escola.save()

				return redirect(reverse_lazy("escola-list"))

		else:
			form = EscolaRegisterForm(request.POST, request.FILES)
			PhoneFormSet = formset_factory(PhoneForm)		
			formset = PhoneFormSet(request.POST, request.FILES)	  

		return render(request, 'subclasses/empresa/escola/edit.html', {'form': form,'formset':formset,'context':context})


class EscolaList(JSONResponseMixin,ListView):
	model = Escola
	template_name = 'subclasses/empresa/escola/list.html'

	def get_context_data(self, **kwargs):
		context = super(EscolaList, self).get_context_data(**kwargs)
		return context 


class EscolaDetail(JSONResponseMixin,DetailView):
	model = Escola
	template_name = 'subclasses/empresa/escola/detail.html'

	def get_context_data(self, **kwargs):
		context = super(EscolaDetail, self).get_context_data(**kwargs)
		return context		


class EscolaDelete(JSONResponseMixin,DeleteView):
	model = Empresa
	success_url = reverse_lazy('escola-list')
	template_name = 'subclasses/empresa/escola/delete.html'

'''
----------------------------------------
			END ESCOLA METHODS
----------------------------------------
'''
