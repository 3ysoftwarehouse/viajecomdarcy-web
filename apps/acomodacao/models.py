from django.db import models

class Acomodacao(models.Model):
	id_acomodacao = models.AutoField(primary_key=True)
	acomodacao_desc = models.CharField(max_length=45, unique=True)
	
	def __str__(self):
		return self.acomodacao_desc
	def __unicode__(self):
		return unicode(self.acomodacao_desc)