from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, RedirectView, View, UpdateView, ListView, DetailView, DeleteView
from datetime import datetime
from .models import PessoaJuridica, PessoaFisica, Pessoa, Fornecedor
from .forms import PessoaFisicaForm, PessoaJuridicaForm

class PessoaRegister(View):
    def get(self, request):
        formfisica = PessoaFisicaForm(prefix='pessoa-fisica', initial={'tipo_pessoa': 'Pessoa Física'})
        formjuridica = PessoaJuridicaForm(prefix='pessoa-juridica', initial={'tipo_pessoa': 'Pessoa Jurídica'})
        context = {'formfisica':formfisica, 'formjuridica':formjuridica}
        return render (request, 'pessoa/register.html', context)

    def post(self, request, *args, **kwargs):
        formfisica = PessoaFisicaForm(prefix='pessoa-fisica')
        formjuridica = PessoaJuridicaForm(prefix='pessoa-juridica')
        context = {'formfisica':formfisica, 'formjuridica':formjuridica}
        if request.POST.get('pessoa-fisica-data_nascimento'):
            request.POST['pessoa-fisica-data_nascimento'] = datetime.strptime(request.POST['pessoa-fisica-data_nascimento'], '%d/%m/%Y').strftime('%Y-%m-%d')
        if request.POST.get('fisica', None):
            formfisica = PessoaFisicaForm(request.POST, prefix='pessoa-fisica')
            if formfisica.is_valid():
                obj = formfisica.save(commit=False)
                obj.tipo_pessoa = 'Pessoa Física'
                obj.save()
                return redirect(reverse_lazy("pessoa-list"))
            else:
                formfisica = PessoaFisicaForm(request.POST, prefix='pessoa-fisica')
                context = {'formfisica':formfisica, 'formjuridica':formjuridica}
                return render (request, 'pessoa/register.html', context)

        if request.POST.get('juridica', None):
            formjuridica = PessoaJuridicaForm(request.POST,prefix='pessoa-juridica')
            if formjuridica.is_valid():
                obj = formjuridica.save(commit=False)
                obj.tipo_pessoa = 'Pessoa Jurídica'
                obj.save()
                return redirect(reverse_lazy("pessoa-list"))
            else:
                formjuridica = PessoaJuridicaForm(request.POST,prefix='pessoa-juridica')
                context = {'formfisica':formfisica, 'formjuridica':formjuridica}
                return render (request, 'pessoa/register.html', context)
        


class PessoaEdit(View):
    def get(self, request, pk):
        pessoa = Pessoa.objects.get(pk=pk)
        if pessoa.tipo_pessoa == 'Pessoa Física':
            pessoa = PessoaFisica.objects.get(cpf_cnpj=pessoa.cpf_cnpj)
            form = PessoaFisicaForm( prefix='pessoa-fisica', instance=pessoa)
        else:
            pessoa = PessoaJuridica.objects.get(cpf_cnpj=pessoa.cpf_cnpj)
            form = PessoaJuridicaForm(prefix='pessoa-juridica', instance=pessoa)
        context = {'form':form, 'pessoa':pessoa}
        return render (request, 'pessoa/edit.html', context)

    def post(self, request, pk, *args, **kwargs):
        pessoa = Pessoa.objects.get(pk=pk)
        tipo =  ''
        if pessoa.tipo_pessoa == 'Pessoa Física':
            tipo = 'Pessoa Física'
            if request.POST.get('pessoa-fisica-data_nascimento'):
                request.POST['pessoa-fisica-data_nascimento'] = datetime.strptime(request.POST['pessoa-fisica-data_nascimento'], '%d/%m/%Y').strftime('%Y-%m-%d')
            pessoa = PessoaFisica.objects.get(cpf_cnpj=pessoa.cpf_cnpj)
            form = PessoaFisicaForm(request.POST, prefix='pessoa-fisica', instance=pessoa)
        else:
            tipo = 'Pessoa Jurídica'
            pessoa = PessoaJuridica.objects.get(cpf_cnpj=pessoa.cpf_cnpj)
            form = PessoaJuridicaForm(request.POST, prefix='pessoa-juridica', instance=pessoa)

        context = {'form':form, 'pessoa':pessoa}
        if form.is_valid():
            obj = form.save(commit=False)
            obj.tipo_pessoa = tipo
            obj.save()
            return redirect(reverse_lazy("pessoa-list"))
        else:
        	return render (request, 'pessoa/edit.html', context)

class PessoaList(ListView):
	model = Pessoa
	template_name = 'pessoa/list.html'

	def get_context_data(self, **kwargs):
		context = super(PessoaList, self).get_context_data(**kwargs)
		return context


class PessoaDelete(DeleteView):
	model = Pessoa
	success_url = reverse_lazy('pessoa-list')
	template_name = 'pessoa/delete.html'


class FornecedorRegister(View):
    def get(self, request):
        formfisica = PessoaFisicaForm(prefix='pessoa-fisica', initial={'tipo_pessoa': 'Pessoa Física'})
        formjuridica = PessoaJuridicaForm(prefix='pessoa-juridica', initial={'tipo_pessoa': 'Pessoa Jurídica'})
        context = {'formfisica':formfisica, 'formjuridica':formjuridica}
        return render (request, 'fornecedor/register.html', context)

    def post(self, request, *args, **kwargs):
        formfisica = PessoaFisicaForm(prefix='pessoa-fisica')
        formjuridica = PessoaJuridicaForm(prefix='pessoa-juridica')
        context = {'formfisica':formfisica, 'formjuridica':formjuridica}
        fornecedor = Fornecedor()
        if request.POST.get('pessoa-fisica-data_nascimento'):
            request.POST['pessoa-fisica-data_nascimento'] = datetime.strptime(request.POST['pessoa-fisica-data_nascimento'], '%d/%m/%Y').strftime('%Y-%m-%d')
        if request.POST.get('fisica', None):
            formfisica = PessoaFisicaForm(request.POST, prefix='pessoa-fisica')
            if formfisica.is_valid():
                obj = formfisica.save(commit=False)
                obj.tipo_pessoa = 'Pessoa Física'
                obj.save()
                fornecedor.pessoa = obj
                fornecedor.save()
                return redirect(reverse_lazy("fornecedor-list"))
            else:
                formfisica = PessoaFisicaForm(request.POST, prefix='pessoa-fisica')
                context = {'formfisica':formfisica, 'formjuridica':formjuridica}
                return render (request, 'fornecedor/register.html', context)

        if request.POST.get('juridica', None):
            formjuridica = PessoaJuridicaForm(request.POST,prefix='pessoa-juridica')
            if formjuridica.is_valid():
                obj = formjuridica.save(commit=False)
                obj.tipo_pessoa = 'Pessoa Jurídica'
                obj.save()
                fornecedor.pessoa = obj
                fornecedor.save()
                return redirect(reverse_lazy("fornecedor-list"))
            else:
                formjuridica = PessoaJuridicaForm(request.POST,prefix='pessoa-juridica')
                context = {'formfisica':formfisica, 'formjuridica':formjuridica}
                return render (request, 'fornecedor/register.html', context)
        


class FornecedorEdit(View):
    def get(self, request, pk):
        fornecedor = Fornecedor.objects.get(pk=pk)
        pessoa = Pessoa.objects.get(pk=fornecedor.pessoa.pk)
        if pessoa.tipo_pessoa == 'Pessoa Física':
            pessoa = PessoaFisica.objects.get(cpf_cnpj=pessoa.cpf_cnpj)
            form = PessoaFisicaForm( prefix='pessoa-fisica', instance=pessoa)
        else:
            pessoa = PessoaJuridica.objects.get(cpf_cnpj=pessoa.cpf_cnpj)
            form = PessoaJuridicaForm(prefix='pessoa-juridica', instance=pessoa)
        context = {'form':form, 'pessoa':pessoa}
        return render (request, 'fornecedor/edit.html', context)

    def post(self, request, pk, *args, **kwargs):
        fornecedor = Fornecedor.objects.get(pk=pk)
        pessoa = Pessoa.objects.get(pk=fornecedor.pessoa.pk)
        tipo =  ''
        if pessoa.tipo_pessoa == 'Pessoa Física':
            tipo = 'Pessoa Física'
            if request.POST.get('pessoa-fisica-data_nascimento'):
                request.POST['pessoa-fisica-data_nascimento'] = datetime.strptime(request.POST['pessoa-fisica-data_nascimento'], '%d/%m/%Y').strftime('%Y-%m-%d')
            pessoa = PessoaFisica.objects.get(cpf_cnpj=pessoa.cpf_cnpj)
            form = PessoaFisicaForm(request.POST, prefix='pessoa-fisica', instance=pessoa)
        else:
            tipo = 'Pessoa Jurídica'
            pessoa = PessoaJuridica.objects.get(cpf_cnpj=pessoa.cpf_cnpj)
            form = PessoaJuridicaForm(request.POST, prefix='pessoa-juridica', instance=pessoa)

        context = {'form':form, 'pessoa':pessoa}
        if form.is_valid():
            obj = form.save(commit=False)
            obj.tipo_pessoa = tipo
            obj.save()
            fornecedor.pessoa = obj
            fornecedor.save()
            return redirect(reverse_lazy("fornecedor-list"))
        else:
            return render (request, 'fornecedor/edit.html', context)

class FornecedorList(ListView):
    model = Fornecedor
    template_name = 'fornecedor/list.html'

    def get_context_data(self, **kwargs):
        context = super(FornecedorList, self).get_context_data(**kwargs)
        return context


class FornecedorDelete(DeleteView):
    model = Fornecedor
    success_url = reverse_lazy('fornecedor-list')
    template_name = 'fornecedor/delete.html'