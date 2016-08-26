from django.db import models
from apps.default.models import Usuario
from apps.subclasses.empresa.agencia.models import Agencia

'''
	SUBCLASSE DE EMISSOR
'''
class Emissor(models.Model):
	id_emissor = models.AutoField(primary_key=True)
	id_usuario = models.OneToOneField(Usuario, on_delete = models.CASCADE,related_name='usuario_name')
	id_agencia = models.OneToOneField(Agencia, on_delete = models.CASCADE,related_name='agencia_name')
	
	def __str__(self):
		return self.id_agencia.id_empresa.nomefantasia
	def __unicode__(self):
		return unicode(self.id_agencia.id_empresa.nomefantasia)