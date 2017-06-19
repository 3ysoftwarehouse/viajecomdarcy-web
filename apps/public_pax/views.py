from django.shortcuts import render
from apps.default.views import JSONResponseMixin
from django.views.generic import CreateView, RedirectView, View, UpdateView, ListView, DetailView, DeleteView
from .models import PerfilPublico
# Create your views here.

class PerfilDetail(JSONResponseMixin,DetailView):
    model = PerfilPublico
    template_name = 'perfil_publico/detail.html'

    def get_context_data(self, **kwargs):
        context = super(PerfilDetail, self).get_context_data(**kwargs)
        return context
