from django.db import models
from apps.default.models import Usuario
from apps.subclasses.empresa.escola.models import Escola


'''
	SUBCLASSE DE PASSAGEIRO
'''
class Passageiro(models.Model):
	id_passageiro = models.AutoField(primary_key=True)
	id_usuario = models.OneToOneField(Usuario, on_delete = models.CASCADE, related_name='passageiro_name')
	id_escola = models.OneToOneField(Escola, on_delete = models.CASCADE,related_name='escola_name',null=True, blank=True)
	matricula = models.IntegerField()
	natularidade = models.CharField(max_length=30,null=True, blank=True)
	observacao = models.CharField(max_length=250,null=True, blank=True)
	def __unicode__(self):
		return self.matricula

