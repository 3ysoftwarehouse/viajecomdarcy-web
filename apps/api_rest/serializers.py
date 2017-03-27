from rest_framework import serializers
import re

from apps.default.models import Usuario

def validateEmail(email):
    p = "^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$"
    if len(email) > 7:
        if re.match(p, email) is not None:
            return 1
    return 0

class LoginSerializer(serializers.Serializer):
	
	email = serializers.CharField(required=True, max_length=100)
	password = serializers.CharField(required=True, max_length=100)
	
	def validate(self, data):
		email = data['email']
		if not  validateEmail(email):
			raise serializers.ValidationError("email invalido")
		if not Usuario.objects.filter(email=email).exists():
			raise serializers.ValidationError("email não existente")
		return data
    