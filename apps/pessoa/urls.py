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
from .views import PessoaRegister, PessoaList, PessoaDetail, PessoaDelete, PessoaEdit
##################################################

urlpatterns = (
	url(r'^dashboard/pessoa/register/$', login_required(PessoaRegister.as_view()), name="pessoa-register"),
	url(r'^dashboard/pessoa/list/$', login_required(PessoaList.as_view()), name="pessoa-list"),
	url(r'^dashboard/pessoa/detail/(?P<pk>\d+)/$', login_required(PessoaDetail.as_view()), name="pessoa-detail"),
	url(r'^dashboard/pessoa/edit/(?P<pk>\d+)/$', login_required(PessoaEdit.as_view()), name="pessoa-edit"),
	url(r'^dashboard/pessoa/delete/(?P<pk>\d+)/$', login_required(PessoaDelete.as_view()), name="pessoa-delete")
)