from django.db import models

class Excursao(models.Model):
	id_excursao = models.AutoField(primary_key=True)
	excurcao_desc = models.CharField(max_length=45,null=False, unique=True)
	is_active = models.BooleanField(default=True)

	def __str__(self):
		return self.excurcao_desc


class Cidade(models.Model):
	id_cidade = models.AutoField(primary_key=True)
	cidade = models.CharField(max_length=100,null=False)

	def __str__(self):
		return self.cidade