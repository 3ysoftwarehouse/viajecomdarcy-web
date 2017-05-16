#-*- coding: utf-8 -*-

##################################################
#				DJANGO IMPORTS                   #
##################################################
from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib.auth.decorators import login_required
##################################################

##################################################
#				CUSTOM IMPORTS                   #
##################################################
from apps.pessoa import views
##################################################

urlpatterns = (
	url(r'^dashboard/pessoa/register/$', login_required(views.PessoaRegister.as_view()), name="pessoa-register"),
	url(r'^dashboard/pessoa/list/$', login_required(views.PessoaList.as_view()), name="pessoa-list"),
	url(r'^dashboard/pessoa/edit/(?P<pk>\d+)/$', login_required(views.PessoaEdit.as_view()), name="pessoa-edit"),
	url(r'^dashboard/pessoa/delete/(?P<pk>\d+)/$', login_required(views.PessoaDelete.as_view()), name="pessoa-delete"),

	url(r'^dashboard/fornecedor/register/$', login_required(views.FornecedorRegister.as_view()), name="fornecedor-register"),
	url(r'^dashboard/fornecedor/list/$', login_required(views.FornecedorList.as_view()), name="fornecedor-list"),
	url(r'^dashboard/fornecedor/edit/(?P<pk>\d+)/$', login_required(views.FornecedorEdit.as_view()), name="fornecedor-edit"),
	url(r'^dashboard/fornecedor/delete/(?P<pk>\d+)/$', login_required(views.FornecedorDelete.as_view()), name="fornecedor-delete")
)