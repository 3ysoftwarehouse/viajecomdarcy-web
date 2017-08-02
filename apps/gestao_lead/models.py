from django.db import models
from apps.subclasses.empresa.escola.models import Escola

# Create your models here.

class Prospect(models.Model):
    nome_completo = models.CharField(max_length=400)
    email = models.EmailField(null=True, blank=True)
    telefone = models.CharField(max_length=100, null=True, blank=True)
    escola = models.ForeignKey(Escola, on_delete=models.DO_NOTHING, null=True, blank=True)
    observacao = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.nome_completo