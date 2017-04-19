from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, RedirectView, View, UpdateView, ListView, DetailView, DeleteView
from .models import PessoaJuridica, PessoaFisica, Pessoa
from .forms import PessoaFisicaForm, PessoaJuridicaForm

class PessoaRegister(View):
    def get(self, request):
        formfisica = PessoaFisicaForm(prefix='pessoa-fisica', initial={'tipo_pessoa': 'Pessoa Física'})
        formjuridica = PessoaJuridicaForm(prefix='pessoa-juridica', initial={'tipo_pessoa': 'Pessoa Jurídica'})
        context = {'formfisica':formfisica, 'formjuridica':formjuridica}
        return render (request, 'pessoa/register.html', context)

    def post(self, request, *args, **kwargs):
        formfisica = PessoaFisicaForm(request.POST, prefix='pessoa-fisica')
        formjuridica = PessoaJuridicaForm(request.POST, prefix='pessoa-juridica')
        context = {'formfisica':formfisica, 'formjuridica':formjuridica}
        if formfisica.is_valid():
            obj = formfisica.save(commit=False)
            obj.tipo_pessoa = 'Pessoa Física'
            obj.save()
            return redirect(reverse_lazy("pessoa-list"))
        elif formjuridica.is_valid():
            obj = formjuridica.save(commit=False)
            obj.tipo_pessoa = 'Pessoa Jurídica'
            obj.save()
            return redirect(reverse_lazy("pessoa-list"))
        else:
        	return render (request, 'pessoa/register.html', context)


class PessoaEdit(View):
    def get(self, request, pk):
    	pessoa = Pessoa.objects.get(pk=pk)
    	if pessoa.tipo_pessoa == 'Pessoa Física':
    		pessoa = PessoaFisica.objects.get(cpf_cnpj=pessoa.cpf_cnpj)
    		form = PessoaFisicaForm(request.POST, prefix='pessoa-fisica', instance=pessoa)
    	else:
    		pessoa = PessoaJuridica.objects.get(cpf_cnpj=pessoa.cpf_cnpj)
    		form = PessoaJuridicaForm(request.POST, prefix='pessoa-juridica', instance=pessoa)

    	context = {'form':form, 'pessoa':pessoa}
    	return render (request, 'pessoa/edit.html', context)

    def post(self, request, pk, *args, **kwargs):

        pessoa = Pessoa.objects.get(pk=pk)
        if pessoa.tipo_pessoa == 'Pessoa Física':
        	pessoa = PessoaFisica.objects.get(cpf_cnpj=pessoa.cpf_cnpj)
        	form = PessoaFisicaForm(request.POST, prefix='pessoa-fisica', instance=pessoa)
        else:
        	pessoa = PessoaJuridica.objects.get(cpf_cnpj=pessoa.cpf_cnpj)
        	form = PessoaJuridicaForm(request.POST, prefix='pessoa-juridica', instance=pessoa)

        context = {'form':form, 'pessoa':pessoa}
        if form.is_valid():
            obj = formfisica.save(commit=False)
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

class PessoaDetail(DetailView):
    model = Pessoa
    template_name = 'pessoa/detail.html'

    def get_context_data(self, **kwargs):
        context = super(PessoaDetail, self).get_context_data(**kwargs)
        if self.object.tipo_pessoa == 'Pessoa Física':
        	context['pessoa'] = PessoaFisica.objects.get(cpf_cnpj=self.object.cpf_cnpj)
        else:
        	context['pessoa'] = PessoaJuridica.objects.get(cpf_cnpj=self.object.cpf_cnpj)
        return context

class PessoaDelete(DeleteView):
	model = Pessoa
	success_url = reverse_lazy('pessoa-list')
	template_name = 'pessoa/delete.html'
