from django.db import models

# Create your models here.
from django.db import models
from model_utils import Choices


# Create your models here.

class Pessoa(models.Model):
	PESSOA_CHOICES = (
		('Pessoa Física', 'Pessoa Fisíca'),
		('Pessoa Jurídica', 'Pessoa Jurídica')
	)

	cpf_cnpj = models.CharField(max_length=20, null=True, blank=True, unique=True)
	nome = models.CharField(max_length=500)
	email = models.EmailField(null=True, blank=True)
	tipo_pessoa = models.CharField(max_length=20, choices=PESSOA_CHOICES, null=True, blank=True)

	def __str__(self):
		return self.nome


class PessoaJuridica(Pessoa):
    razao_social = models.CharField(max_length=400, null=True, blank=True)

    def __str__(self):
        return self.nome


class PessoaFisica(Pessoa):
    data_nascimento = models.DateField(null=True, blank=True)
    rg = models.CharField(max_length=12, null=True, blank=True)
    orgaoemissor = models.CharField(max_length=45, null=True, blank=True)

    def __str__(self):
        return self.nome


class Fornecedor(models.Model):
   pessoa = models.OneToOneField(Pessoa)
   
   def __str__(self):
       return self.pessoa.nome