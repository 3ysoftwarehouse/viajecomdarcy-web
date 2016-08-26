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
from .views import ExcursaoRegister, ExcursaoList, ExcursaoDetail, ExcursaoDelete, ExcursaoEdit
##################################################


urlpatterns = (
	# CLIENTE URLS
	url(r'^dashboard/excursao/register/$', login_required(ExcursaoRegister.as_view()), name="excursao-register"),
	url(r'^dashboard/excursao/list/$', login_required(ExcursaoList.as_view()), name="excursao-list"),
	url(r'^dashboard/excursao/detail/(?P<pk>\d+)/$', login_required(ExcursaoDetail.as_view()), name="excursao-detail"),
	url(r'^dashboard/excursao/edit/(?P<pk>\d+)/$', login_required(ExcursaoEdit.as_view()), name="excursao-edit"),
	url(r'^dashboard/excursao/delete/(?P<pk>\d+)/$', login_required(ExcursaoDelete.as_view()), name="excursao-delete"),
)
