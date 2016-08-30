from django.db import models
from apps.moeda.models import Moeda
from apps.excursao.models import Excursao, Opcional, Cidade

class Pacote(models.Model):
	id_pacote = models.AutoField(primary_key=True)
	id_excursao = models.ForeignKey(Excursao, on_delete=models.CASCADE,related_name='excursao_name')
	id_moeda = models.ForeignKey(Moeda, on_delete=models.CASCADE,related_name='moeda_name')
	pacote_nome = models.CharField(max_length=45)
	pacote_desc = models.CharField(max_length=200)
	is_active = models.BooleanField(default=True)
	pacote_preco = models.DecimalField(max_digits=10, decimal_places=2)
	pacote_taxa = models.DecimalField(max_digits=10, decimal_places=2)
	pacote_daybyday = models.TextField()
	pacote_obs = models.TextField()
	
	def __str__(self):
		return self.pacote_nome
	def __unicode__(self):
		return unicode(self.pacote_nome)

class PacoteOpcional(models.Model):
	id_pacote_opcional = models.AutoField(primary_key=True)
	id_pacote = models.ForeignKey(Pacote, on_delete=models.CASCADE,related_name='pacote_name')
	id_opcional = models.ForeignKey(Opcional, on_delete=models.CASCADE,related_name='opcional_name')


class PacoteCidade(models.Model):
	id_pacote_cidade = models.AutoField(primary_key=True)
	id_pacote = models.ForeignKey(Pacote, on_delete=models.CASCADE,related_name='pacote_cidade_name')
	id_cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE,related_name='cidade_name')
	qtd_dias = models.IntegerField()
	ordem = models.IntegerField()
	