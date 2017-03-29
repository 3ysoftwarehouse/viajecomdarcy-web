from django.db import models
#from django.utils.translation import ugettext_lazy as _

from apps.moeda.models import Moeda

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


class Opcional(models.Model):
	id_opcional  = models.AutoField(primary_key=True)
	opcional_desc = models.CharField(max_length=46, null=False, unique=True)
	opcional_preco = models.DecimalField(max_digits=10, decimal_places=2, null=False)
	id_moeda = models.ForeignKey('moeda.Moeda', on_delete=models.CASCADE)
	taxa_remessa = models.DecimalField(max_digits=6, decimal_places=4)
	
	def __str__(self):
		return self.opcional_desc

	def percentage(self):
		if self.taxa_remessa:
			taxa = self.taxa_remessa * 100;
			return "%.1f" % taxa
		else:
			return 0