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
from .views import MoedaRegister, MoedaEdit, MoedaList, MoedaDetail, MoedaDelete
##################################################


urlpatterns = (
	# STARTUP URLS
	url(r'^dashboard/moeda/register/$', login_required(MoedaRegister.as_view()), name="moeda-register"),
	url(r'^dashboard/moeda/list/$', login_required(MoedaList.as_view()), name="moeda-list"),
	url(r'^dashboard/moeda/detail/(?P<pk>\d+)/$', login_required(MoedaDetail.as_view()), name="moeda-detail"),
	url(r'^dashboard/moeda/edit/(?P<pk>\d+)/$', login_required(MoedaEdit.as_view()), name="moeda-edit"),
	url(r'^dashboard/moeda/delete/(?P<pk>\d+)/$', login_required(MoedaDelete.as_view()), name="moeda-delete")
)
