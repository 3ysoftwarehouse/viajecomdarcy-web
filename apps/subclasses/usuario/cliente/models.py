from django.db import models
from apps.default.models import Usuario, Endereco

class Cliente(models.Model):
	id_cliente = models.AutoField(primary_key=True)
	nome_pai = models.CharField(max_length=45,null=True, blank=True)
	nome_mae = models.CharField(max_length=45,null=True, blank=True)
	naturalidade = models.CharField(max_length=45,null=True, blank=True)
	numero_dependentes = models.IntegerField()
	tipo_residencia = models.CharField(max_length=20,null=True, blank=True)
	usuario = models.OneToOneField(Usuario, on_delete = models.CASCADE, related_name='cliente_name')
	dt_emissao_rg = models.DateTimeField(null=True, blank=True)
	tempo_residencia = models.CharField(max_length=20,null=True, blank=True)
	empresa = models.CharField(max_length=20,null=True, blank=True)
	telefone = models.CharField(max_length=20,null=True, blank=True)
	dt_admissao = models.DateTimeField(null=True, blank=True)
	cargo = models.CharField(max_length=20,null=True, blank=True)
	principal_renda = models.CharField(max_length=20,null=True, blank=True)
	outra_renda = models.CharField(max_length=20,null=True, blank=True)
	patrimonio = models.CharField(max_length=20,null=True, blank=True)
	banco = models.CharField(max_length=20,null=True, blank=True)
	agencia = models.CharField(max_length=20,null=True, blank=True)
	conta = models.CharField(max_length=20,null=True, blank=True)
	dt_banco = models.DateTimeField(null=True, blank=True)
	telefone_banco = models.CharField(max_length=20,null=True, blank=True)
	cnpj_empresa = models.CharField(max_length=20,null=True, blank=True)
	id_endereco_empresa = models.ForeignKey('default.Endereco', on_delete=models.DO_NOTHING, null=True, blank=True)

	def __str__(self):
		return self.usuario.nome
