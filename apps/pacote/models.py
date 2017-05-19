from django.db import models
from apps.moeda.models import Moeda
from apps.excursao.models import Excursao, Opcional, Cidade
from apps.acomodacao.models import Acomodacao



class Pacote(models.Model):
	id_pacote = models.AutoField(primary_key=True)
	id_excursao = models.ForeignKey(Excursao, on_delete=models.CASCADE,related_name='excursao_name')
	id_moeda = models.ForeignKey(Moeda, on_delete=models.CASCADE,related_name='moeda_name')
	pacote_nome = models.CharField(max_length=45)
	pacote_desc = models.TextField(max_length=200)
	is_active = models.BooleanField(default=True)
	pacote_preco = models.DecimalField(max_digits=10, decimal_places=2)
	pacote_taxa = models.DecimalField(max_digits=10, decimal_places=2)
	pacote_daybyday = models.TextField(null=True, blank=True)
	pacote_obs = models.TextField(null=True, blank=True)
	taxa_remessa = models.DecimalField(max_digits=6, decimal_places=4)
	data_prevista = models.DateField(null=True, blank=True)
	
	def __str__(self):
		return self.pacote_nome
		
	def __unicode__(self):
		return unicode(self.pacote_nome)

	def percentage(self):
		if self.taxa_remessa:
			taxa = self.taxa_remessa * 100;
			return "%.1f" % taxa
		else:
			return 0


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
	

class PacoteAcomadacao(models.Model):
	id_pacote_acomodacao = models.AutoField(primary_key=True)
	id_pacote = models.ForeignKey(Pacote, on_delete=models.CASCADE,related_name='pacote_acomodacao_name')
	id_acomodacao = models.ForeignKey(Acomodacao, on_delete=models.CASCADE,related_name='acomadacao_name')
	id_moeda = models.ForeignKey(Moeda, on_delete=models.CASCADE,related_name='pacote_acomodacao_moeda_name')
	preco = models.DecimalField(max_digits=10, decimal_places=2)

