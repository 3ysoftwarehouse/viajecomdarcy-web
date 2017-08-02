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
from .views import *
##################################################


urlpatterns = (
	# PROSPECT URLS
	url(r'^dashboard/prospect/register/$', login_required(ProspectRegister.as_view()), name="prospect-register"),
	url(r'^dashboard/prospect/list/$', login_required(ProspectList.as_view()), name="prospect-list"),
	url(r'^dashboard/prospect/detail/(?P<pk>\d+)/$', login_required(ProspectDetail.as_view()), name="prospect-detail"),
	url(r'^dashboard/prospect/edit/(?P<pk>\d+)/$', login_required(ProspectEdit.as_view()), name="prospect-edit"),
	url(r'^dashboard/prospect/delete/(?P<pk>\d+)/$', login_required(ProspectDelete.as_view()), name="prospect-delete"),
)
