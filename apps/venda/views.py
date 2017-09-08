#-*- coding: utf-8 -*-

##################################################
#               DJANGO IMPORTS                   #
##################################################
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render,redirect
from django.template.loader import render_to_string
from django.views.generic import CreateView, RedirectView, View, UpdateView, ListView, DetailView, DeleteView
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.http import (HttpResponse,
                         HttpResponseForbidden,
                         HttpResponseBadRequest)
from django.forms import formset_factory
##################################################



##################################################
#               CUSTOM IMPORTS                   #
##################################################
from .models import Reserva, StatusReserva, StatusReservaPassageiro, ReservaPassageiro, PassageiroOpcional
from .forms import ReservaForm, ReservaPassageiroForm, FiltroReservaForm, ReservaOpcionaisForm, NovaReservaForm, NovaReservaPassageiroForm
from apps.default.views import JSONResponseMixin
from apps.subclasses.usuario.emissor.models import Emissor
from apps.subclasses.usuario.cliente.models import Cliente
from apps.subclasses.usuario.passageiro.models import Passageiro
from apps.acomodacao.models import Acomodacao
from apps.excursao.models import Excursao, Opcional
from apps.moeda.models import Moeda
from apps.pacote.models import Pacote, PacoteAcomadacao, PacoteOpcional
from apps.subclasses.usuario.emissor.views import get_emissor
##################################################

class ReservaNova(JSONResponseMixin,View):
    def get(self, request):
        context = {}

        try:
            emissor = Emissor.objects.get(id_usuario=request.user.id_usuario)
        except Emissor.DoesNotExist:
            context['Emissor'] = "não encontrado"

        if not context:
            form = NovaReservaForm()
            context['form'] = form
            return render (request, 'venda/reserva/register-novo.html', context)
        else:
            return redirect(reverse_lazy("reserva-list", kwargs={'context':context}))

    def post(self, request, *args, **kwargs):
        context = {}

        try:
            emissor = Emissor.objects.get(id_usuario=request.user.id_usuario)
        except Emissor.DoesNotExist:
            context['Emissor'] = "não encontrado"

        try:
            id_status_reserva = StatusReserva.objects.get(descricao="ABERTO")
        except:
            id_status_reserva = StatusReserva()
            id_status_reserva.descricao = "ABERTO"
            id_status_reserva.save()

        try:
            id_status_reserva_passageiro = StatusReservaPassageiro.objects.get(descricao="RESERVADO")
        except:
            id_status_reserva_passageiro = StatusReservaPassageiro()
            id_status_reserva_passageiro.descricao = "RESERVADO"
            id_status_reserva_passageiro.save()

        if not context:
            form = NovaReservaForm(request.POST)
            context['form'] = form
            if form.is_valid():
                reserva = form.save(commit=False)
                reserva.id_emissor = emissor
                reserva.id_status_reserva = id_status_reserva
                reserva.id_agencia = emissor.id_agencia
                reserva.save()

                passageiro = form.cleaned_data.get('id_passageiro')

                reserva_passageiro = ReservaPassageiro()
                reserva_passageiro.id_reserva = reserva
                reserva_passageiro.id_passageiro = passageiro
                reserva_passageiro.id_status_reserva_passageiro = id_status_reserva_passageiro
                reserva_passageiro.id_escola = passageiro.id_escola
                reserva_passageiro.save()

                return redirect(reverse_lazy("reserva-edit", kwargs={'pk': reserva.pk}))
            else:
                return render (request, 'venda/reserva/register-novo.html', context)
        else:
            return redirect(reverse_lazy("reserva-list", kwargs={'context':context}))



class ReservaRegister(JSONResponseMixin,View):
    def get(self, request, pk):
        formset = formset_factory(ReservaPassageiroForm,extra=0)
        try:
            id_status_reserva_passageiro = StatusReservaPassageiro.objects.get(descricao="RESERVADO").pk
        except:
            id_status_reserva_passageiro = StatusReservaPassageiro()
            id_status_reserva_passageiro.descricao = "RESERVADO"
            id_status_reserva_passageiro.save()

        initial_data = [
            {'id_status_reserva_passageiro': id_status_reserva_passageiro},
        ]
        passageiros = ReservaPassageiro.objects.filter(id_reserva = pk).order_by('id_passageiro')
        form = ReservaForm()
        form_opcional = ReservaOpcionaisForm()
        form_passageiro = ReservaPassageiroForm()
        return render (request, 'venda/reserva/register_2.html', { 'form':form,'form_passageiro':form_passageiro, 'passageiros': passageiros,'form_opcional':form_opcional})

    def post(self, request, pk=None, *args, **kwargs):
        formset = formset_factory(ReservaPassageiroForm)
        formset = formset(request.POST)
        form = ReservaForm(request.POST)

        context = {}        
        data = request.POST

        if not data.get('id_cliente', None):
            context['Cliente'] = "não pode ser vazio"
        else:
            id_cliente = Cliente.objects.get(pk=data['id_cliente'])
        if not data.get('id_status_reserva', None):
            #context['Status da Reserva'] = "não pode ser vazio"
            pass
        else:
            id_status_reserva = StatusReserva.objects.get(pk=data['id_status_reserva'])

        listPassageiros = []
        if formset.is_valid():
            for f in formset:
                value = f.cleaned_data
                listPassageiros.append([
                    value.get('id_passageiro'),
                    value.get('id_pacote'),
                    value.get('id_status_reserva_passageiro'),
                    value.get('reserva_passageiro_preco'),
                    value.get('reserva_passageiro_cambio'),
                    value.get('reserva_passageiro_obs'),

                    # FEATURE 805 MODIFICAÇÔES
                    value.get('id_acomodacao_pacote'),
                    value.get('preco_acomodacao'),
                    value.get('registro_interno'),
                    value.get('desconto')
                    ]
                    )


                if not value.get('id_passageiro'):
                    context['Passagerio'] = "não pode ser vazio"
                if not value.get('id_pacote'):
                    context['Pacote'] = "não pode ser vazio"
                #if not value.get('id_status_reserva_passageiro'):
                #   context['Status da Reserva do Passafeiro'] = "não pode ser vazio"
                if not value.get('reserva_passageiro_preco'):
                    context['Preço'] = "não pode ser vazio"
                if not value.get('reserva_passageiro_cambio'):
                    context['Cambio'] = "não pode ser vazio"
                #if not value.get('reserva_passageiro_obs'):
                #   context['Obs'] = "não pode ser vazio"

                # FEATURE 805 MODIFICAÇÔES
                if not value.get('id_acomodacao_pacote'):
                    context['Acomodação'] = "não pode ser vazio"
                if not value.get('preco_acomodacao'):
                    context['Preço Acomodação'] = "não pode ser vazio"
        else:
            for erro in formset.errors:                 
                context['error'] = erro
            pass

        try:
            emissor = Emissor.objects.get(id_usuario=request.user.id_usuario)
        except Emissor.DoesNotExist:
            context['Emissor'] = "não encontrado"

        if not context:

            reserva = Reserva.objects.get(pk=pk)
            reserva.id_cliente = id_cliente
            reserva.save()

            for value in listPassageiros:

                reservapassageiro = ReservaPassageiro() 
                reservapassageiro.id_reserva =  reserva
                reservapassageiro.id_passageiro = value[0]
                reservapassageiro.id_pacote = value[1]
                reservapassageiro.id_status_reserva_passageiro = value[2]
                reservapassageiro.id_escola = value[0].id_escola
                reservapassageiro.reserva_passageiro_preco = value[3]
                reservapassageiro.id_moeda = value[1].id_moeda
                reservapassageiro.reserva_passageiro_cambio = value[4]
                if value[5]:
                    reservapassageiro.reserva_passageiro_obs = value[5]

                # FEATURE 805 MODIFICAÇÔES
                reservapassageiro.id_acomodacao_pacote = value[6]
                reservapassageiro.preco_acomodacao = value[7]
                if value[8]:
                    reservapassageiro.registro_interno = value[8]
                if value[9]:
                    reservapassageiro.desconto = value[9]

                reservapassageiro.save()


            return redirect(reverse_lazy('passageiro-opcional', kwargs = {'pk' : reserva.pk, }))

        return render (request, 'venda/reserva/register.html', { 'form':form, 'formset':formset, 'context':context })


class ReservaEdit(JSONResponseMixin,View):
    def get(self, request, pk=None, *args, **kwargs):
        context = {}

        try:
            emissor = Emissor.objects.get(id_usuario=request.user.id_usuario)
        except Emissor.DoesNotExist:
            context['Emissor'] = "não encontrado"

        if not context:
            reserva = Reserva.objects.get(pk=self.kwargs['pk'])
            reservapassageiro = ReservaPassageiro.objects.get(id_reserva=reserva.pk)

            opcionais_inicial = {'id_passageiro':reservapassageiro.id_passageiro}

            form = NovaReservaPassageiroForm(instance=reservapassageiro)
            form_opcional = ReservaOpcionaisForm(initial=opcionais_inicial)
            context['form'] = form
            context['form_opcional'] = form_opcional
            context['reservapassageiro'] = reservapassageiro
            return render (request, 'venda/reserva/edit-novo.html', context)
        else:
            return redirect(reverse_lazy("reserva-list", kwargs={'context':context}))

    def post(self, request, pk=None, *args, **kwargs):
        context = {}

        try:
            emissor = Emissor.objects.get(id_usuario=request.user.id_usuario)
        except Emissor.DoesNotExist:
            context['Emissor'] = "não encontrado"

        if not context:
            reserva = Reserva.objects.get(pk=self.kwargs['pk'])
            reservapassageiro = ReservaPassageiro.objects.get(id_reserva=reserva.pk)

            form = NovaReservaPassageiroForm(request.POST, instance=reservapassageiro)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.save()
                return redirect(reverse_lazy("reserva-list"))
            else:
                opcionais_inicial = {'id_passageiro':reservapassageiro.id_passageiro}
                form_opcional = ReservaOpcionaisForm(initial=opcionais_inicial)
                context['form'] = form
                context['form_opcional'] = form_opcional
                context['reservapassageiro'] = reservapassageiro

                print(request.POST)
                print(form.errors)
                print(form_opcional.errors)
                return render (request, 'venda/reserva/edit-novo.html', context)
        else:
            return redirect(reverse_lazy("reserva-list", kwargs={'context':context}))


class ReservaList(JSONResponseMixin, View):
    def get(self, request, **kwargs):
        form = FiltroReservaForm()

        emissor = get_emissor(self)
        if emissor:
            object_list = Reserva.objects.filter(id_emissor=emissor.pk, id_agencia=emissor.id_agencia.pk).order_by('-id_reserva')[:1]
        else:
            object_list = Reserva.objects.all()

        return render (request, 'venda/reserva/list.html', {'object_list':object_list,'form':form})

    def post(self, request, pk=None, *args, **kwargs):
        form = FiltroReservaForm(request.POST)
        data_inicio = None
        data_fim = None
        if form.is_valid():
            data_inicio = form.cleaned_data['data_inicio']
            data_fim = form.cleaned_data['data_fim']

        emissor = get_emissor(self)
        if emissor:
            if data_inicio and data_fim:
                object_list = Reserva.objects.filter(id_emissor=emissor.pk, id_agencia=emissor.id_agencia.pk,data_reserva__gte=data_inicio, data_reserva__lte=data_fim)
            elif data_inicio:
                object_list = Reserva.objects.filter(id_emissor=emissor.pk, id_agencia=emissor.id_agencia.pk,data_reserva__gte=data_inicio)
            elif data_fim:
                object_list = Reserva.objects.filter(id_emissor=emissor.pk, id_agencia=emissor.id_agencia.pk,data_reserva__lte=data_fim)
            else:
                object_list = Reserva.objects.filter(id_emissor=emissor.pk, id_agencia=emissor.id_agencia.pk)
        else:
            if data_inicio and data_fim:
                object_list = Reserva.objects.filter(data_reserva__gte=data_inicio, data_reserva__lte=data_fim)
            elif data_inicio:
                object_list = Reserva.objects.filter(data_reserva__gte=data_inicio)
            elif data_fim:
                object_list = Reserva.objects.filter(data_reserva__lte=data_fim)
            else:
                object_list = Reserva.objects.all()

        return render (request, 'venda/reserva/list.html', {'object_list':object_list,'form':form})


class ReservaDetail(JSONResponseMixin,DetailView):
    model = Reserva
    template_name = 'venda/reserva/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ReservaDetail, self).get_context_data(**kwargs)
        return context

class ReservaDelete(JSONResponseMixin,DeleteView):
    model = Reserva
    success_url = reverse_lazy('reserva-list')
    template_name = 'venda/reserva/delete.html' 

class ExcursaoPacoteJson(JSONResponseMixin,View):
    def get(self, request, *args, **kwargs):
        if self.kwargs:
            try:
                pacotes = Pacote.objects.filter(id_excursao=self.kwargs['pk']).values('id_pacote','pacote_nome', 'pacote_preco')
            except:
                pacotes = None
        if pacotes:
            return JsonResponse({'data':list(pacotes)})
        else:
            return JsonResponse({'data':'error'})

class PacoteMoedaJson(JSONResponseMixin,View):
    def get(self, request, *args, **kwargs):
        if self.kwargs:
            try:
                pacote = Pacote.objects.filter(pk=self.kwargs['pk']).values('id_pacote','pacote_preco', 'id_moeda','id_moeda__moeda_desc', 'id_moeda__moeda_cambio')
                acomodacao = PacoteAcomadacao.objects.filter(id_pacote=self.kwargs['pk']).values('id_acomodacao','id_acomodacao__acomodacao_desc', 'preco')
            except:
                pacotes = None
                acomodacao = None
        if pacote:
            return JsonResponse({'pacote':list(pacote), 'acomodacao':list(acomodacao)})
        else:
            return JsonResponse({'pacote':'error'})



class PassageiroOpc(JSONResponseMixin,View):
    def get(self, request, pk=None):
        reserva = Reserva.objects.get(pk=self.kwargs['pk'])
        reservapassageiros = ReservaPassageiro.objects.filter(id_reserva=reserva.pk)

        id_passageiros = []
        for passageiro in reservapassageiros:
            id_passageiros.append(passageiro.id_passageiro.pk)
            pass

        formset = formset_factory(ReservaOpcionaisForm)
        formset = formset(form_kwargs={'id_passageiros': id_passageiros})

        return render (request, 'venda/passageiro/register.html', {'formset':formset, 'reserva':reserva})
    
    def post(self, request, pk=None, *args, **kwargs):
        reserva = Reserva.objects.get(pk=self.kwargs['pk'])
        reservapassageiros = ReservaPassageiro.objects.filter(id_reserva=reserva.pk)

        id_passageiros = []
        for passageiro in reservapassageiros:
            id_passageiros.append(passageiro.id_passageiro.pk)
            pass

        formset = formset_factory(ReservaOpcionaisForm)
        formset = formset(request.POST, form_kwargs={'id_passageiros': id_passageiros})

        context = {}        

        listOpcionais = []
        if formset.is_valid():
            for f in formset:
                value = f.cleaned_data
                listOpcionais.append([
                    value.get('id_moeda'),
                    value.get('id_reserva_passageiro'),
                    value.get('id_opcional'),
                    value.get('preco_reserva_opcional')
                ])

                if not value.get('id_passageiro'):
                    context['Passagerio'] = "não pode ser vazio"
                #if not value.get('id_moeda'):
                #   context['Moeda'] = "não pode ser vazio"
                #if not value.get('id_reserva_passageiro'):
                #   context['Reserva do Passageiro'] = "não pode ser vazio"
                if not value.get('id_opcional'):
                    context['Opcional'] = "não pode ser vazio"
                if not value.get('preco_reserva_opcional'):
                    context['Preço'] = "não pode ser vazio"
        else:
            for erro in formset.errors:                 
                context['error'] = erro
            pass

        if not context:

            for value in listOpcionais:

                opcional = PassageiroOpcional() 
                opcional.id_moeda = value[0]
                opcional.id_reserva_passageiro = value[1]
                opcional.id_opcional = value[2]
                opcional.preco_reserva_opcional = value[3]
                opcional.save()

            return redirect(reverse_lazy('reserva-list'))
        
        return render (request, 'venda/passageiro/register.html', {'formset':formset, 'reserva':reserva, 'context':context})

class PassageiroOpcJson(JSONResponseMixin,View):
    def get(self, request, *args, **kwargs):
        id_reserva = self.kwargs['id_reserva']
        id_passageiro = self.kwargs['id_passageiro']
        reservapassageiro = ReservaPassageiro.objects.get(id_reserva=id_reserva,id_passageiro=id_passageiro)
        if reservapassageiro:
            opicionais = PacoteOpcional.objects.filter(id_pacote=reservapassageiro.id_pacote).values('id_opcional','id_opcional__opcional_desc')
            return JsonResponse({
                'id_reserva_passageiro':reservapassageiro.id_reserva_passageiro,
                'reserva_passageiro_obs':reservapassageiro.reserva_passageiro_obs, 
                'opicionais':list(opicionais)
            })
        else:
            return JsonResponse({'data':'error'})

class PassageiroOpcMoedaJson(JSONResponseMixin,View):
    def get(self, request, *args, **kwargs):
        id_reserva_passageiro = self.kwargs['id_reserva_passageiro']
        id_opcional = self.kwargs['id_opcional']

        opcional = Opcional.objects.get(id_opcional=id_opcional)
        reservapassageiro = ReservaPassageiro.objects.get(id_reserva_passageiro=id_reserva_passageiro)
        
        if reservapassageiro and opcional:
            pacoteopcional = PacoteOpcional.objects.get(id_pacote=reservapassageiro.id_pacote, id_opcional=opcional.id_opcional)
            moeda = pacoteopcional.id_pacote.id_moeda
            return JsonResponse({
                'id_moeda':moeda.id_moeda,
                'moeda_desc':moeda.moeda_desc
            })
        else:
            return JsonResponse({'data':'error'})


def finalizarAgendamento(request, pk=None, cl=None):
    try:
        try:
            id_status_reserva = StatusReserva.objects.get(descricao="RESERVADO")
        except:
            id_status_reserva = StatusReserva()
            id_status_reserva.descricao = "RESERVADO"
            id_status_reserva.save()
            
        id_cliente = Cliente.objects.get(pk=cl)
        reserva = Reserva.objects.get(pk=pk)
        reserva.id_status_reserva = id_status_reserva
        reserva.id_cliente = id_cliente
        reserva.save()
        return JsonResponse({'message':'success', 'status':'success'})
    except Exception as e:
        return JsonResponse({'message':str(e), 'status':'error'})


''' ADD PASSAGEIRO A RESERVAPASSAGEIRO '''
def addPassageiroToReserva(request,pk):
    if request.method == 'POST':
        form = ReservaPassageiroForm(request.POST)
        
        id_passageiro = request.POST.get('id_passageiro')
        id_pacote = request.POST.get('id_pacote')
        id_status_reserva_passageiro = request.POST.get('id_status_reserva_passageiro')
        reserva_passageiro_preco = request.POST.get('reserva_passageiro_preco')
        reserva_passageiro_cambio = request.POST.get('reserva_passageiro_cambio')
        reserva_passageiro_obs = request.POST.get('reserva_passageiro_obs')
        id_acomodacao_pacote = request.POST.get('id_acomodacao_pacote')
        preco_acomodacao = request.POST.get('preco_acomodacao')
        registro_interno = request.POST.get('registro_interno')
        desconto = request.POST.get('desconto')
            
        try:
            status_reserva_passageiro = StatusReservaPassageiro.objects.get(descricao="RESERVADO")
            passageiro = Passageiro.objects.get(id_passageiro = id_passageiro)
            pacote = Pacote.objects.get(id_pacote = id_pacote)
            reserva = Reserva.objects.get(pk=pk)
            reservapassageiro = ReservaPassageiro()
            reservapassageiro.id_reserva =  reserva
            reservapassageiro.id_passageiro = passageiro
            reservapassageiro.id_pacote = pacote
            reservapassageiro.id_status_reserva_passageiro = status_reserva_passageiro
            reservapassageiro.id_escola = passageiro.id_escola
            reservapassageiro.reserva_passageiro_preco = reserva_passageiro_preco
            reservapassageiro.id_moeda = pacote.id_moeda
            reservapassageiro.reserva_passageiro_cambio = reserva_passageiro_cambio
            if reserva_passageiro_obs:
                reservapassageiro.reserva_passageiro_obs = reserva_passageiro_obs

            # FEATURE 805 MODIFICAÇÔES
            reservapassageiro.id_acomodacao_pacote = Acomodacao.objects.get(id_acomodacao = id_acomodacao_pacote)
            reservapassageiro.preco_acomodacao = preco_acomodacao
            if registro_interno:
                reservapassageiro.registro_interno = registro_interno
            if desconto:
                reservapassageiro.desconto = desconto

            reservapassageiro.save()
            passageiros = ReservaPassageiro.objects.filter(id_reserva = pk).order_by('id_passageiro')
            html = render_to_string('venda/reserva/reservas_snippet.html', {'passageiros':passageiros})
            return JsonResponse({'status':'success', 'message':'success','html':html})
        except Exception as e:
            return JsonResponse({'message':str(e), 'status':'error'})

def editPassageiroReserva(request):
    if request.method == 'POST':
        form = ReservaPassageiroForm(request.POST)
        
        id_reserva_passageiro = request.POST.get('id_reserva_passageiro')
        id_passageiro = request.POST.get('id_passageiro')
        id_pacote = request.POST.get('id_pacote')
        id_status_reserva_passageiro = request.POST.get('id_status_reserva_passageiro')
        reserva_passageiro_preco = request.POST.get('reserva_passageiro_preco')
        reserva_passageiro_cambio = request.POST.get('reserva_passageiro_cambio')
        reserva_passageiro_obs = request.POST.get('reserva_passageiro_obs')
        id_acomodacao_pacote = request.POST.get('id_acomodacao_pacote')
        preco_acomodacao = request.POST.get('preco_acomodacao')
        registro_interno = request.POST.get('registro_interno')
        desconto = request.POST.get('desconto')

        try:
            status_reserva_passageiro = StatusReservaPassageiro.objects.get(descricao="RESERVADO")
            passageiro = Passageiro.objects.get(id_passageiro = id_passageiro)
            pacote = Pacote.objects.get(id_pacote = id_pacote)
            #reserva = Reserva.objects.get(pk=pk)
            reservapassageiro = ReservaPassageiro.objects.get(pk=id_reserva_passageiro)
            #reservapassageiro.id_reserva =  reserva
            reservapassageiro.id_passageiro = passageiro
            reservapassageiro.id_pacote = pacote
            reservapassageiro.id_status_reserva_passageiro = status_reserva_passageiro
            reservapassageiro.id_escola = passageiro.id_escola
            reservapassageiro.reserva_passageiro_preco = reserva_passageiro_preco
            reservapassageiro.id_moeda = pacote.id_moeda
            reservapassageiro.reserva_passageiro_cambio = reserva_passageiro_cambio
            if reserva_passageiro_obs:
                reservapassageiro.reserva_passageiro_obs = reserva_passageiro_obs

            # FEATURE 805 MODIFICAÇÔES
            reservapassageiro.id_acomodacao_pacote = Acomodacao.objects.get(id_acomodacao = id_acomodacao_pacote)
            reservapassageiro.preco_acomodacao = preco_acomodacao
            if registro_interno:
                reservapassageiro.registro_interno = registro_interno
            if desconto:
                reservapassageiro.desconto = desconto

            reservapassageiro.save()
            passageiros = ReservaPassageiro.objects.filter(id_reserva = reservapassageiro.id_reserva).order_by('id_passageiro')
            html = render_to_string('venda/reserva/reservas_snippet.html', {'passageiros':passageiros})
            return JsonResponse({'status':'success', 'message':'success','html':html})
        except Exception as e:
            return JsonResponse({'message':str(e), 'status':'error'})


def addOpcionalPassageiro(request, pk):
    if request.method == 'POST':
        reserva = Reserva.objects.get(pk=pk)
        id_moeda = request.POST.get('id_moeda')
        id_reserva_passageiro = request.POST.get('id_reserva_passageiro')
        id_opcional = request.POST.get('id_opcional')
        preco_reserva_opcional = request.POST.get('preco_reserva_opcional')
        reservapassageiro = ReservaPassageiro.objects.get(id_reserva_passageiro=id_reserva_passageiro)
        try:
            opcional = PassageiroOpcional() 
            opcional.id_moeda = Moeda.objects.get(id_moeda = id_moeda)
            opcional.id_reserva_passageiro = reservapassageiro
            opcional.id_opcional = Opcional.objects.get(id_opcional = id_opcional)
            opcional.preco_reserva_opcional = preco_reserva_opcional
            opcional.save()
            reservapassageiro.passageiro_opcional.add(opcional)
            passageiros = ReservaPassageiro.objects.filter(id_reserva = pk).order_by('id_passageiro')
            html = render_to_string('venda/reserva/reservas_snippet.html', {'passageiros':passageiros})
            return JsonResponse({'status':'success', 'message':'success','html':html})
        except Exception as e:
            return JsonResponse({'message':str(e), 'status':'error'})

