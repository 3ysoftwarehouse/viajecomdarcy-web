#-*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class Projeto(models.Model):
	id_projeto = models.AutoField(primary_key=True)
	nome = models.CharField(max_length=45)
	logo = models.ImageField(upload_to="default/project",null=True, blank=True)
	website = models.URLField(max_length=100, null=True)
	def __str__(self):
		return self.nome

class Genero(models.Model):
    id_genero = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=45)
    abreviacao = models.CharField(max_length=1)
    def __str__(self):
        return self.descricao

class Logradouro(models.Model):
	id_logradouro = models.AutoField(primary_key=True)
	cep = models.CharField(max_length=10)
	nome = models.CharField(max_length=100)
	bairro = models.CharField(max_length=45)
	cidade = models.CharField(max_length=20)
	estado = models.CharField(max_length=2)
	pais = models.CharField(max_length=45)
	def __str__(self):
		return self.nome

class Endereco(models.Model):
	id_endereco = models.AutoField(primary_key=True)
	id_logradouro = models.ForeignKey('Logradouro', on_delete=models.DO_NOTHING)
	numero = models.IntegerField()
	complemento = models.CharField(max_length=45, null=True, blank=True)
	pontoreferencia = models.CharField(max_length=45, null=True, blank=True)
	def __str__(self):
		return self.id_logradouro.nome
		
class TipoEmpresa(models.Model):
	id_tipo_empresa = models.AutoField(primary_key=True)
	descricao = models.CharField(max_length=45)
	def __str__(self):
		return self.descricao

class Empresa(models.Model):
	id_empresa = models.AutoField(primary_key=True)
	id_endereco = models.ForeignKey('Endereco', on_delete=models.DO_NOTHING, null=True, blank=True)
	id_tipo_empresa = models.ForeignKey('TipoEmpresa', on_delete=models.DO_NOTHING, null=True, blank=True)
	razaosocial = models.CharField(max_length=100, null=True, blank=True)
	nomefantasia = models.CharField(max_length=100)
	cnpj = models.CharField(max_length=20,null=True, blank=True)
	verificada = models.BooleanField(default=True)
	ie = models.CharField(max_length=45, null=True, blank=True)
	def __str__(self):
		return self.nomefantasia

class TipoUsuario(models.Model):
	id_tipo_usuario= models.AutoField(primary_key=True)
	descricao = models.CharField(max_length=45)
	def __str__(self):
		return self.descricao

class TipoRelacao(models.Model):
	id_tipo_relacao = models.AutoField(primary_key=True)
	descricao = models.CharField(max_length=45)
	def __str__(self):
		return self.descricao

class TipoRelacaoEmpresa(models.Model):
	id_tipo_relacao_empresa = models.AutoField(primary_key=True)
	descricao = models.CharField(max_length=45)
	def __str__(self):
		return self.descricao

class TipoDocumento(models.Model):
	id_tipo_documento = models.AutoField(primary_key=True)
	descricao = models.CharField(max_length=45)
	def __str__(self):
		return self.descricao

class TipoTelefone(models.Model):
	id_tipo_Telefone = models.AutoField(primary_key=True)
	descricao = models.CharField(max_length=45)
	def __str__(self):
		return self.descricao

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Cria e salva um usuario.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email), 
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Cria e salva um super usuario.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser):
	id_usuario = models.AutoField(primary_key=True)
	id_tipo_usuario = models.ForeignKey('TipoUsuario', on_delete=models.DO_NOTHING, null=True, blank=True)
	id_endereco = models.ForeignKey('Endereco', on_delete=models.DO_NOTHING, null=True, blank=True)
	id_genero = models.ForeignKey('Genero', on_delete=models.DO_NOTHING, null=True, blank=True)
	nome = models.CharField(max_length=45,null=True, blank=True)
	sobrenome = models.CharField(max_length=45,null=True, blank=True)
	nomecompleto = models.CharField(max_length=100,null=True, blank=True)
	email = models.CharField('email',max_length=75,unique=True,default='')
	cpf = models.CharField(max_length=14, null=True, blank=True)
	data_nascimento = models.DateField(null=True, blank=True)
	rg = models.CharField(max_length=12, null=True, blank=True)
	orgaoemissor = models.CharField(max_length=45,null=True, blank=True)
	foto = models.ImageField(upload_to="default/users", null=True, blank=True)
	is_active = models.BooleanField(default=False)
	is_admin = models.BooleanField(default=False)

	objects = UserManager()

	USERNAME_FIELD = 'email'
	# REQUIRED_FIELDS = ['date_of_birth']

	def get_full_name(self):
	    # The user is identified by their email address
	    return self.nomecompleto

	def get_short_name(self):
	    # The user is identified by their email address
	    return self.nome

	def __str__(self): # __unicode__ on Python 2
	    return self.email

	def has_perm(self, perm, obj=None):
	    "Does the user have a specific permission?"
	    # Simplest possible answer: Yes, always
	    return True

	def has_module_perms(self, app_label):
	    "Does the user have permissions to view the app `app_label`?"
	    # Simplest possible answer: Yes, always
	    return True

	@property
	def is_staff(self):
	    "Is the user a member of staff?"
	    # Simplest possible answer: All admins are staff
	    return self.is_admin

	def __str__(self):
		return self.email

class TelefoneUsuario(models.Model):
	id_telefone_usuario = models.AutoField(primary_key=True)
	id_tipo_telefone = models.ForeignKey('TipoTelefone', on_delete=models.CASCADE, null=True, blank=True)
	id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
	numero = models.CharField(max_length=11)
	def __str__(self):
		return self.numero

class TelefoneEmpresa(models.Model):
	id_telefone_empresa = models.AutoField(primary_key=True)
	id_tipo_telefone = models.ForeignKey('TipoTelefone', on_delete=models.CASCADE, null=True, blank=True)
	id_empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE, null=True, blank=True)
	numero = models.CharField(max_length=11)
	ramal = models.CharField(max_length=4, null=True, blank=True)
	nome_contato = models.CharField(max_length=45, null=True, blank=True)
	def __unicode__(self):
		return self.numero

class UsuarioEmpresa(models.Model):
	id_usuario_empresa = models.AutoField(primary_key=True)
	id_visao = models.ForeignKey('Visao', on_delete=models.DO_NOTHING)
	id_usuario = models.ForeignKey('Usuario', on_delete=models.DO_NOTHING)
	id_empresa = models.ForeignKey('Empresa', on_delete=models.DO_NOTHING)
	ativo = models.BooleanField(default=True)
	def __str__(self):
		return self.ativo

class Visao(models.Model):
	id_visao = models.AutoField(primary_key=True)
	descricao = models.CharField(max_length=45)
	def __str__(self):
		return self.descricao

class RelacaoEmpresa(models.Model):
	id_relacao_empresa = models.AutoField(primary_key=True)
	id_empresa_1 = models.ForeignKey('TipoEmpresa', on_delete=models.DO_NOTHING)
	id_relacao_empresa = models.ForeignKey('TipoRelacaoEmpresa', on_delete=models.DO_NOTHING)
	data_criacao = models.DateTimeField(default=timezone.now)
	def __str__(self):
		return self.criacao_data

class RelacaoUsuario(models.Model):
	id_relacao_usuario = models.AutoField(primary_key=True)
	id_usuario_1 = models.ForeignKey('TipoUsuario', on_delete=models.DO_NOTHING)
	id_tipo_relacao_empresa = models.ForeignKey('TipoRelacaoEmpresa', on_delete=models.DO_NOTHING)
	data_criacao = models.DateTimeField(default=timezone.now)
	def __str__(self):
		return self.razaosocial

class Documento(models.Model):
	id_documento = models.AutoField(primary_key=True)
	id_usuario = models.ForeignKey('Usuario', on_delete=models.DO_NOTHING)
	id_tipo_documento = models.ForeignKey('TipoDocumento', on_delete=models.DO_NOTHING)
	anexo = models.ImageField(upload_to="default/documents")
	datahora = models.DateTimeField(default=timezone.now)
	