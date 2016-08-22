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
from .views import EmployeeRegister, EmployeeList, EmployeeDetail, EmployeeDelete, EmployeeEdit
##################################################


urlpatterns = (
	# EMPLOYEE URLS
	url(r'^dashboard/employee/register/$', login_required(EmployeeRegister.as_view()), name="employee-register"),
	url(r'^dashboard/employee/list/$', login_required(EmployeeList.as_view()), name="employee-list"),
	url(r'^dashboard/employee/detail/(?P<pk>\d+)/$', login_required(EmployeeDetail.as_view()), name="employee-detail"),
	url(r'^dashboard/employee/edit/(?P<pk>\d+)/$', login_required(EmployeeEdit.as_view()), name="employee-edit"),
	url(r'^dashboard/employee/delete/(?P<pk>\d+)/$', login_required(EmployeeDelete.as_view()), name="employee-delete"),
)
