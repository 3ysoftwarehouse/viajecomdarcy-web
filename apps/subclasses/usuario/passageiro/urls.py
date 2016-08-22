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
from .views import PassageiroRegister, PassageiroList, PassageiroDetail, PassageiroDelete, PassageiroEdit
##################################################


urlpatterns = (
	# EMPLOYEE URLS
	url(r'^dashboard/passageiro/register/$', login_required(PassageiroRegister.as_view()), name="passageiro-register"),
	url(r'^dashboard/passageiro/list/$', login_required(PassageiroList.as_view()), name="passageiro-list"),
	url(r'^dashboard/passageiro/detail/(?P<pk>\d+)/$', login_required(PassageiroDetail.as_view()), name="passageiro-detail"),
	url(r'^dashboard/passageiro/edit/(?P<pk>\d+)/$', login_required(PassageiroEdit.as_view()), name="passageiro-edit"),
	url(r'^dashboard/passageiro/delete/(?P<pk>\d+)/$', login_required(PassageiroDelete.as_view()), name="passageiro-delete"),
)
