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
from .forms import AgenciaRegisterForm
from apps.default.forms import PhoneForm # PHONE FORMS
from apps.default.views import JSONResponseMixin, validaCNPJ
from .models import Agencia
##################################################


'''
----------------------------------------
			AGENCIA METHODS
----------------------------------------
''' 


class AgenciaRegister(JSONResponseMixin,View):
	def get(self, request):
		form = AgenciaRegisterForm
		formset = formset_factory(PhoneForm)
		return render (request, 'subclasses/empresa/agencia/register.html', {'form':form,'formset':formset})

	def post(self, request, *args, **kwargs):
		context = {}
		if request.method == 'POST':

			PhoneFormSet = formset_factory(PhoneForm)		
			formset = PhoneFormSet(request.POST, request.FILES)
			form = AgenciaRegisterForm(request.POST, request.FILES)
	
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
			#representante = request.POST['representante']

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
			#if not representante:
			#	context['representante'] = ' cannot be empty !'
			
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
				agencia = Agencia()
				agencia.id_empresa = empresa
				agencia.save()
					
				return redirect(reverse_lazy("agencia-list"))

		else:
			PhoneFormSet = formset_factory(PhoneForm)		
			formset = PhoneFormSet(request.POST, request.FILES)
			form = AgenciaRegisterForm(request.POST, request.FILES)

		return render(request, 'subclasses/empresa/agencia/register.html', {'form': form, 'formset':formset ,'context':context})


class AgenciaEdit(JSONResponseMixin,View):
	def get(self, request, pk=None):
		agencia = Agencia.objects.get(pk=pk)
		empresa = Empresa.objects.get(pk=agencia.id_empresa.pk)
		telefones = TelefoneEmpresa.objects.filter(id_empresa=empresa.pk)

		
		PhoneFormSet = formset_factory(PhoneForm,extra=0)
		

		data = []
		for telefone in telefones:
			data.append({'tipo_telefone':telefone.id_tipo_telefone,'numero':telefone.numero,'ramal':telefone.ramal,'nome_contato':telefone.nome_contato})
		
				
		formset = PhoneFormSet(
			initial=data
			)

		form = AgenciaRegisterForm(
			initial={
			'razaosocial': agencia.id_empresa.razaosocial,
			'nomefantasia': agencia.id_empresa.nomefantasia,
			'cnpj': agencia.id_empresa.cnpj,
			'verificada': agencia.id_empresa.verificada,
			'ie': agencia.id_empresa.ie,
			'tipo_empresa': agencia.id_empresa.id_tipo_empresa,
			'cep' :  agencia.id_empresa.id_endereco.id_logradouro.cep,
		    'rua' :  agencia.id_empresa.id_endereco.id_logradouro.nome,
		    'bairro' :  agencia.id_empresa.id_endereco.id_logradouro.bairro,
		    'cidade' :  agencia.id_empresa.id_endereco.id_logradouro.cidade,
		    'estado' :  agencia.id_empresa.id_endereco.id_logradouro.estado,
		    'pais' : agencia.id_empresa.id_endereco.id_logradouro.pais,
		    'numeroed' :  agencia.id_empresa.id_endereco.numero,
		    'complemento' : agencia.id_empresa.id_endereco.complemento,
		    'pontoreferencia' :  agencia.id_empresa.id_endereco.pontoreferencia,
		    
			# EXTRAS
		    #'representante' : startup.representante,
			}
			)

		return render (request, 'subclasses/empresa/agencia/edit.html', {'form':form ,'formset':  formset})

	def post(self, request, pk=None, *args, **kwargs):
		context = {}
		if request.method == 'POST':		    
			form = AgenciaRegisterForm(request.POST, request.FILES)
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
			#representante = request.POST['representante']

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
			#if not representante:
			#	context['representante'] = ' cannot be empty !'

			if not context:

				agencia = Agencia.objects.get(pk=pk)

				empresa = Empresa.objects.get(pk=agencia.id_empresa.pk)
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
				#agencia.representante = representante
				#agencia.save()

				return redirect(reverse_lazy("agencia-list"))

		else:
			form = AgenciaRegisterForm(request.POST, request.FILES)
			PhoneFormSet = formset_factory(PhoneForm)		
			formset = PhoneFormSet(request.POST, request.FILES)	  

		return render(request, 'subclasses/empresa/agencia/edit.html', {'form': form,'formset':formset,'context':context})



class AgenciaList(JSONResponseMixin,ListView):
	model = Agencia
	template_name = 'subclasses/empresa/agencia/list.html'

	def get_context_data(self, **kwargs):
		context = super(AgenciaList, self).get_context_data(**kwargs)
		return context      


class AgenciaDetail(JSONResponseMixin,DetailView):
	model = Agencia
	template_name = 'subclasses/empresa/agencia/detail.html'

	def get_context_data(self, **kwargs):
		context = super(AgenciaDetail, self).get_context_data(**kwargs)
		return context


class AgenciaDelete(JSONResponseMixin,DeleteView):
	model = Empresa
	success_url = reverse_lazy('agencia-list')
	template_name = 'subclasses/empresa/agencia/delete.html'

'''
----------------------------------------
			END AGENCIA METHODS
----------------------------------------
'''