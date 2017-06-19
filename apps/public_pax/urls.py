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
from .views import PerfilDetail
##################################################


urlpatterns = (
	# STARTUP URLS
	url(r'^pax/3/(?P<pk>\d+)/$', PerfilDetail.as_view(), name="perfil-detail"),
)