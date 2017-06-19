from django.db import models

# Create your models here.

class PerfilPublico(models.Model):
    data = models.DateField(null=True, blank=True)
    pax = models.CharField(max_length=400)
    foto = models.ImageField(upload_to="default/pax_public", null=True, blank=True, default='')
    grupo = models.CharField(max_length=400)
    emissor = models.CharField(max_length=400)
    agencia = models.CharField(max_length=400, null=True, blank=True)
    escola = models.CharField(max_length=400, null=True, blank=True)
    data_nascimento = models.DateField()
    cel_pax = models.CharField(max_length=400, null=True, blank=True)
    email_pax = models.EmailField(null=True, blank=True)
    resp_pax = models.CharField(max_length=400)
    fone_resp = models.CharField(max_length=400)
    email_resp = models.EmailField(null=True, blank=True)
    cod_r1 = models.IntegerField(null=True, blank=True)
    cod_r2 = models.IntegerField(null=True, blank=True)
    cod_r3 = models.IntegerField(null=True, blank=True)
    roomates = models.ManyToManyField('PerfilPublico', symmetrical=True, null=True, blank=True)
    opcionais = models.CharField(max_length=400)
    ficha_medica = models.FileField(upload_to="default/ficha_medica", null=True, blank=True, default='')



    def __str__(self):
        return self.pax



