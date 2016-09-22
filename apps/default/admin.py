#-*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Usuario, Projeto, Genero, Logradouro, Endereco, TipoEmpresa, Empresa, TipoUsuario, TipoRelacao, TipoRelacaoEmpresa, TipoDocumento, TipoTelefone, TelefoneUsuario, TelefoneEmpresa, UsuarioEmpresa,Visao, RelacaoEmpresa, RelacaoUsuario,Documento

from .forms import UserCreationForm, UserChangeForm

class UserAdmin(BaseUserAdmin):
    # Formularios para adicionar ou alterar instancias dos usuarios
    form = UserChangeForm
    add_form = UserCreationForm

    # Os campos a serem no User model.
    list_display = ('email', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('nome','sobrenome','foto','email', 'password','is_active')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    # Campos a serem exibidos no cadastro de um usuario no painel admin.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

# Registra as alteracoes no painel admin
admin.site.register(Usuario, UserAdmin)
admin.site.register(Projeto)
admin.site.register(Genero)
admin.site.register(Logradouro)
admin.site.register(Endereco)
admin.site.register(TipoEmpresa)
admin.site.register(Empresa)
admin.site.register(TipoUsuario)
admin.site.register(TipoRelacao)
admin.site.register(TipoRelacaoEmpresa)
admin.site.register(TipoDocumento)
admin.site.register(TipoTelefone)
admin.site.register(TelefoneUsuario)
admin.site.register(TelefoneEmpresa)
admin.site.register(UsuarioEmpresa)
admin.site.register(Visao)
admin.site.register(RelacaoEmpresa)
admin.site.register(RelacaoUsuario)
admin.site.register(Documento)


admin.site.unregister(Group)
