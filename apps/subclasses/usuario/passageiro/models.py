from django.db import models

'''
	SUBCLASSE DE PASSAGEIRO
'''
class Passageiro(models.Model):
	id_passageiro = models.AutoField(primary_key=True)
	id_usuario = models.ForeignKey('default.Usuario', on_delete = models.CASCADE, related_name='passageiro_name')
	id_escola = models.ForeignKey('escola.Escola', on_delete = models.CASCADE,related_name='escola_name',null=True, blank=True)
	matricula = models.IntegerField()
	natularidade = models.CharField(max_length=30,null=True, blank=True)
	observacao = models.CharField(max_length=250,null=True, blank=True)
	id_emissor = models.ForeignKey('emissor.Emissor', on_delete=models.DO_NOTHING, null=True, blank=True)
	id_agencia = models.ForeignKey('agencia.Agencia', on_delete=models.DO_NOTHING, null=True, blank=True)
	numero_passaporte = models.CharField(max_length=10,null=True, blank=True)
	data_validade_passaporte = models.DateField(null=True, blank=True)
	
	def __str__(self):
		if self.id_usuario.sobrenome:
			return str(self.id_usuario.nome + ' ' + self.id_usuario.sobrenome)
		else:
			return str(self.id_usuario.nome)
		
