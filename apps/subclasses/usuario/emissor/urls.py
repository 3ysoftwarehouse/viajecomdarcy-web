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
from .views import EmissorRegister, EmissorList, EmissorDetail, EmissorDelete, EmissorEdit
##################################################


urlpatterns = (
	# EMPLOYEE URLS
	url(r'^dashboard/emissor/register/$', login_required(EmissorRegister.as_view()), name="emissor-register"),
	url(r'^dashboard/emissor/list/$', login_required(EmissorList.as_view()), name="emissor-list"),
	url(r'^dashboard/emissor/detail/(?P<pk>\d+)/$', login_required(EmissorDetail.as_view()), name="emissor-detail"),
	url(r'^dashboard/emissor/edit/(?P<pk>\d+)/$', login_required(EmissorEdit.as_view()), name="emissor-edit"),
	url(r'^dashboard/emissor/delete/(?P<pk>\d+)/$', login_required(EmissorDelete.as_view()), name="emissor-delete"),
)
