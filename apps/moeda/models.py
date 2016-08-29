from django.db import models


class Moeda(models.Model):
	id_moeda = models.AutoField(primary_key=True)
	moeda_desc = models.CharField(max_length=15, unique=True)
	moeda_cambio = models.DecimalField(max_digits=4, decimal_places=3)
	moeda_ultimaatualizacao = models.DateTimeField(auto_now_add=True)
	moeda_simbolo = models.CharField(max_length=2)
	
	def __str__(self):
		return self.moeda_desc
	def __unicode__(self):
		return unicode(self.moeda_desc)