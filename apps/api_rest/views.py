from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import permissions, status, generics
from rest_framework.parsers import MultiPartParser, FormParser
from django.contrib.auth import authenticate, login, logout
from datetime import datetime, timedelta, date
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope
import requests
import re

from apps.default.models import Usuario
from oauth2_provider.models import Application
from .serializers import LoginSerializer



class Login(APIView):
	def post(self, request, format=None):
		context = {}
		user = ""
		serializer = LoginSerializer(data=request.data)
		if serializer.is_valid():
			email = serializer.data['email']
			password = serializer.data['password']
			user = authenticate(email=email, password=password)
			try:
				app = Application.objects.all()[0]
			except:
				context['msg'] = 'Application não encontrado'
				return Response(context, status=500)
			if user:
				login(request, user)
				client_auth = requests.auth.HTTPBasicAuth(app.client_id,app.client_secret)
				post_data = {"grant_type": "password", "username": email, "password": password}
				headers = {"User-Agent": "ChangeMeClient/0.1 by YourUsername"}
				#response = requests.post("http:///o/token/", auth=client_auth, data=post_data, headers=headers)
				response = requests.post("http://127.0.0.1:8000/en/o/token/", auth=client_auth, data=post_data, headers=headers)
				context = {
					'name':user.nomecompleto,
					'email':user.email,
					'token':response.json()['access_token']
				}
				return Response(context, status=200)
			else:
				context['status'] = 'incorrectPassword'
				context['msg'] = 'Senha incorreta.'
				return Response(context, status=409)
			return Response(context, status=200)
		else:
			return Response(serializer.errors, status=500)
