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
from apps.default.models import Projeto, Usuario, Empresa, Logradouro, Endereco, TipoEmpresa, TipoTelefone, TelefoneUsuario, TipoUsuario, Genero # MODELS
from .models import Emissor # MODELS
from apps.subclasses.empresa.agencia.models import Agencia # MODELS
from .forms import EmissorRegisterForm
from apps.default.forms import PhoneForm # PHONE FORMS
from apps.default.views import JSONResponseMixin
##################################################



'''
----------------------------------------
			EMISSOR METHODS
----------------------------------------
''' 

class EmissorRegister(JSONResponseMixin,View):
	def get(self, request):
		form = EmissorRegisterForm
		formset = formset_factory(PhoneForm)
		return render (request, 'subclasses/usuario/emissor/register.html', {'form':form, 'formset':formset})

	def post(self, request, *args, **kwargs):
		context = {}
		if request.method == 'POST':		    
			form = EmissorRegisterForm(request.POST,request.FILES)
			PhoneFormSet = formset_factory(PhoneForm)		
			formset = PhoneFormSet(request.POST, request.FILES)
			
			nome = request.POST['nome']
			sobrenome = request.POST['sobrenome']
			email = request.POST['email']
			password = request.POST['password']
			tipo_usuario = request.POST['tipo_usuario']
			genero = request.POST['genero']
			data_nascimento = request.POST['data_nascimento']
			cpf = request.POST['cpf']
			rg = request.POST['rg']
			orgaoemissor = request.POST['orgaoemissor']
			foto = request.FILES.get('foto', None)

			cep = request.POST['cep']
			rua = request.POST['rua']
			bairro = request.POST['bairro']
			cidade = request.POST['cidade']
			estado = request.POST['estado']
			pais = request.POST['pais']

			numero = request.POST['numero']
			complemento = request.POST['complemento']
			pontoreferencia = request.POST['pontoreferencia']

			# EXTRAS
			id_agencia = request.POST['id_agencia']

			if data_nascimento:
				data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y').strftime('%Y-%m-%d')
			else:
				data_nascimento = None
			
			if not nome:
				context['error_msg'] = 'nome cannot be empty !'
			if not sobrenome:
				context['error_msg'] = 'sobrenome cannot be empty !'
			if not email:
				context['error_msg'] = 'email cannot be empty !'
			if not password:
				context['error_msg'] = 'password cannot be empty !'

			if not tipo_usuario:
				context['error_msg'] = 'tipo_usuario cannot be empty !'
			if not genero:
				context['error_msg'] = 'genero cannot be empty !'
			if not data_nascimento:
				context['error_msg'] = 'data_nascimento cannot be empty !'
			if not cpf:
				context['error_msg'] = 'cpf cannot be empty !'
			if not rg:
				context['error_msg'] = 'rg cannot be empty !'
			if not orgaoemissor:
				context['error_msg'] = 'orgaoemissor cannot be empty !'
			'''
			if not foto:
				context['error_msg'] = 'foto cannot be empty !'
			'''
			if not cep:
				context['error_msg'] = 'cep cannot be empty !'
			if not rua:
				context['error_msg'] = 'rua cannot be empty !'
			if not bairro:
				context['error_msg'] = 'bairro cannot be empty !'
			if not cidade:
				context['error_msg'] = 'cidade cannot be empty !'
			if not estado:
				context['error_msg'] = 'estado cannot be empty !'
			if not pais:
				context['error_msg'] = 'pais cannot be empty !'
			if not numero:
				context['error_msg'] = 'numero cannot be empty !'
			if not complemento:
				context['error_msg'] = 'complemento cannot be empty !'
			if not pontoreferencia:
				context['error_msg'] = 'pontoreferencia cannot be empty !'

			# EXTRAS
			if not id_agencia:
				context['error_msg'] = 'id_agencia cannot be empty !'

			listphones = []

			if formset.is_valid():
				for f in formset:
					phone = f.cleaned_data
					listphones.append([phone.get('tipo_telefone'),phone.get('numero')])

					if not phone.get('tipo_telefone'):
						context['Tipo Telefone'] = ' cannot be empty !'
					if not phone.get('numero'):
						context['Numero'] = ' cannot be empty !'
			else:
				for erro in formset.errors:					
					context['error'] = erro
				pass

			if not context:

				id_logradouro = Logradouro()
				id_logradouro.cep = cep
				id_logradouro.nome = nome
				id_logradouro.bairro = bairro
				id_logradouro.cidade = cidade
				id_logradouro.estado = estado
				id_logradouro.pais = pais
				id_logradouro.save()

				id_endereco = Endereco()
				id_endereco.id_logradouro = id_logradouro
				id_endereco.numero = numero
				id_endereco.complemento = complemento
				id_endereco.pontoreferencia = pontoreferencia
				id_endereco.save()

				usuario = Usuario.objects.create_user(email, password)
				usuario.nome = nome
				usuario.sobrenome = sobrenome
				usuario.nomecompleto = nome +" "+sobrenome
				usuario.id_tipo_usuario = TipoUsuario.objects.get(pk=tipo_usuario)
				usuario.id_genero = Genero.objects.get(pk=genero)
				usuario.data_nascimento = data_nascimento
				usuario.cpf = cpf
				usuario.rg = rg
				usuario.orgaoemissor = orgaoemissor
				usuario.foto = foto
				usuario.id_endereco = id_endereco
				usuario.is_active =  False
				usuario.save()

				for listphone in listphones:
					id_tipo_telefone = TipoTelefone.objects.filter(descricao=listphone[0])[0]			
					teluser = TelefoneUsuario()
					teluser.id_tipo_telefone = id_tipo_telefone
					teluser.id_usuario = usuario
					teluser.numero = listphone[1]
					teluser.save()

				agencia = Agencia.objects.filter(id_agencia=id_agencia)[0]

				emissor = Emissor()
				emissor.id_usuario = usuario
				emissor.id_agencia = agencia
				emissor.save()

				return redirect(reverse_lazy("emissor-list"))

			else:
				form = EmissorRegisterForm(request.POST,request.FILES)
				PhoneFormSet = formset_factory(PhoneForm)		
				formset = PhoneFormSet(request.POST, request.FILES)

		return render(request, 'subclasses/usuario/employee/register.html', {'form': form, 'formset':formset})


class EmissorEdit(JSONResponseMixin,View):
	def get(self, request, pk=None):
		emissor = Emissor.objects.get(pk=pk)
		usuario = Usuario.objects.get(pk=emissor.id_usuario.pk)
		id_endereco = Endereco.objects.get(pk=usuario.id_endereco.pk)
		id_logradouro = Logradouro.objects.get(pk=id_endereco.id_logradouro.pk)

		telefones = TelefoneUsuario.objects.filter(id_usuario=usuario.pk)
		PhoneFormSet = formset_factory(PhoneForm,extra=0)
		
		data = []
		for telefone in telefones:
			data.append({'tipo_telefone':telefone.id_tipo_telefone,'numero':telefone.numero})
		
				
		formset = PhoneFormSet(
			initial=data
			)

		form = EmissorRegisterForm(
			initial={
			'nome': usuario.nome,
			'sobrenome': usuario.sobrenome,
			'email': usuario.email,
			'tipo_usuario' : usuario.id_tipo_usuario, 
			'genero' : usuario.id_genero,
			'data_nascimento' : usuario.data_nascimento,
			'cpf' : usuario.cpf,
			'rg' : usuario.rg,
			'orgaoemissor' : usuario.orgaoemissor,
			'foto' : usuario.foto,
			'cep' : id_logradouro.cep, 
			'rua' : id_logradouro.nome,
			'bairro' : id_logradouro.bairro,
			'cidade' : id_logradouro.cidade,
			'estado' : id_logradouro.estado,
			'pais' : id_logradouro.pais,
			'numero': id_endereco.numero,
			'complemento': id_endereco.complemento,
			'pontoreferencia': id_endereco.pontoreferencia,
			'id_agencia': emissor.id_agencia,		
			}
			)
		return render (request, 'subclasses/usuario/emissor/edit.html', {'form':form,'formset':formset})

	def post(self, request, pk=None, *args, **kwargs):
		context = {}
		if request.method == 'POST':		    
			form = EmissorRegisterForm(request.POST,request.FILES)
			PhoneFormSet = formset_factory(PhoneForm)		
			formset = PhoneFormSet(request.POST, request.FILES)

			nome = request.POST['nome']
			sobrenome = request.POST['sobrenome']
			email = request.POST['email']
			tipo_usuario = request.POST['tipo_usuario']
			genero = request.POST['genero']
			data_nascimento = request.POST['data_nascimento']
			cpf = request.POST['cpf']
			rg = request.POST['rg']
			orgaoemissor = request.POST['orgaoemissor']
			foto = request.FILES.get('foto', None)

			cep = request.POST['cep']
			rua = request.POST['rua']
			bairro = request.POST['bairro']
			cidade = request.POST['cidade']
			estado = request.POST['estado']
			pais = request.POST['pais']

			numero = request.POST['numero']
			complemento = request.POST['complemento']
			pontoreferencia = request.POST['pontoreferencia']

			id_agencia = request.POST['id_agencia']

			listphones = []

			if formset.is_valid():
				for f in formset:
					phone = f.cleaned_data
					listphones.append([phone.get('tipo_telefone'),phone.get('numero')])

					if not phone.get('tipo_telefone'):
						context['Tipo Telefone'] = ' cannot be empty !'
					if not phone.get('numero'):
						context['Numero'] = ' cannot be empty !'
			else:
				for erro in formset.errors:					
					context['error'] = erro
				pass

			
			if not nome:
				context['Nome'] = ' cannot be empty !'
			if not sobrenome:
				context['Sobrenome'] = ' cannot be empty !'
			if not email:
				context['E-mail'] = ' cannot be empty !'
			if not tipo_usuario:
				context['Tipo'] = ' cannot be empty !'
			if not genero:
				context['Genero'] = ' cannot be empty !'
			if not data_nascimento:
				context['Data de nascimento'] = ' cannot be empty !'
			if not cpf:
				context['CPF'] = ' cannot be empty !'
			if not rg:
				context['RG'] = ' cannot be empty !'
			if not orgaoemissor:
				context['Orgão'] = ' cannot be empty !'
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
			if not numero:
				context['Número'] = ' cannot be empty !'
			if not complemento:
				context['Complemento'] = ' cannot be empty !'
			if not pontoreferencia:
				context['Refêrencia'] = ' cannot be empty !'
			if not id_agencia:
				context['id_agencia'] = ' cannot be empty !'

			if not context:

				emissor = Emissor.objects.get(pk=pk)
				usuario = Usuario.objects.get(pk=emissor.id_usuario.pk)
				id_endereco = Endereco.objects.get(pk=usuario.id_endereco.pk)
				id_logradouro = Logradouro.objects.get(pk=id_endereco.id_logradouro.pk)

				telefones = TelefoneUsuario.objects.filter(id_usuario=usuario.pk)
				for telefone in telefones:
					telefone.delete()
	
				id_logradouro.cep = cep
				id_logradouro.nome = nome
				id_logradouro.bairro = bairro
				id_logradouro.cidade = cidade
				id_logradouro.estado = estado
				id_logradouro.pais = pais
				id_logradouro.save()

				
				id_endereco.id_logradouro = id_logradouro
				id_endereco.numero = numero
				id_endereco.complemento = complemento
				id_endereco.pontoreferencia = pontoreferencia
				id_endereco.save()

				
				usuario.nome = nome
				usuario.sobrenome = sobrenome
				usuario.nomecompleto = nome +" "+sobrenome
				usuario.id_tipo_usuario = TipoUsuario.objects.get(pk=tipo_usuario)
				usuario.id_genero = Genero.objects.get(pk=genero)
				usuario.data_nascimento = data_nascimento
				usuario.cpf = cpf
				usuario.rg = rg
				usuario.orgaoemissor = orgaoemissor
				usuario.foto = foto
				usuario.id_endereco = id_endereco
				usuario.is_active =  False
				usuario.save()

				agencia = Agencia.objects.filter(id_agencia=id_agencia)[0]

				emissor.id_usuario = usuario
				emissor.id_agencia = agencia
				emissor.save()

				for listphone in listphones:
					id_tipo_telefone = TipoTelefone.objects.filter(descricao=listphone[0])[0]			
					teluser = TelefoneUsuario()
					teluser.id_tipo_telefone = id_tipo_telefone
					teluser.id_usuario = usuario
					teluser.numero = listphone[1]
					teluser.save()

				return redirect(reverse_lazy("emissor-list"))

			else:
				form = EmployeeRegisterForm(request.POST)
				PhoneFormSet = formset_factory(PhoneForm)		
				formset = PhoneFormSet(request.POST, request.FILES)

		return render (request, 'subclasses/usuario/emissor/edit.html', {'form':form ,'formset':formset,'context':context})



class EmissorList(JSONResponseMixin,ListView):
	queryset = Emissor.objects.all()
	template_name = 'subclasses/usuario/emissor/list.html'

	def get_context_data(self, **kwargs):

		context = super(EmissorList, self).get_context_data(**kwargs)
		emissores = Emissor.objects.all()
		lists = []

		for value in emissores:
			telefone = TelefoneUsuario.objects.filter(id_usuario=value.id_usuario)
			if telefone:
				lists.append([value,telefone[0]])
			else:
				lists.append([value,telefone])

		context["emissores"] = lists

		return context


class EmissorDetail(JSONResponseMixin,DetailView):
	model = Emissor
	template_name = 'subclasses/usuario/emissor/detail.html'

	def get_context_data(self, **kwargs):
		context = super(EmissorDetail, self).get_context_data(**kwargs)
		return context


class EmissorDelete(JSONResponseMixin,DeleteView):
	model = Usuario
	success_url = reverse_lazy('emissor-list')
	template_name = 'subclasses/usuario/emissor/delete.html'

'''
----------------------------------------
			END EMISSOR METHODS
----------------------------------------
'''