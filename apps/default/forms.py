#-*- coding: utf-8 -*-
from django import forms
from django.conf import settings
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import Usuario, Empresa, Genero, TipoUsuario, TipoEmpresa, TipoTelefone, TelefoneEmpresa # MODELS


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('email',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Usuario
        fields = ('email', 'password', 'is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]



class LoginForm(forms.Form):
    email = forms.EmailField(label='Email:', max_length=75)
    password = forms.CharField(label='Senha:', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Digite seu email'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Digite sua senha'
        pass


class RegisterForm(forms.Form):
    nome = forms.CharField(label='Nome:', max_length=45)
    sobrenome = forms.CharField(label='Sobrenome:', max_length=45)
    email = forms.EmailField(label='Email:', max_length=75)
    password = forms.CharField(label='Senha:', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs['class'] = 'form-control'
        self.fields['nome'].widget.attrs['placeholder'] = 'Digite seu nome'
        self.fields['sobrenome'].widget.attrs['class'] = 'form-control'
        self.fields['sobrenome'].widget.attrs['placeholder'] = 'Digite seu sobrenome'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Digite seu email'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Digite sua senha'


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('nome','sobrenome','nomecompleto','id_tipo_usuario','id_endereco','id_genero','cpf','data_nascimento','rg','orgaoemissor','foto')

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs['class'] = 'form-control'
        self.fields['nome'].widget.attrs['placeholder'] = 'Digite seu nome'
        self.fields['sobrenome'].widget.attrs['class'] = 'form-control'
        self.fields['sobrenome'].widget.attrs['placeholder'] = 'Digite seu sobrenome'
        self.fields['nomecompleto'].widget.attrs['class'] = 'form-control'
        self.fields['nomecompleto'].widget.attrs['placeholder'] = 'Digite seu nome completo'
        self.fields['id_genero'].widget.attrs['class'] = 'form-control'
        self.fields['id_genero'].widget.attrs['placeholder'] = 'Escolha seu genero'
        self.fields['data_nascimento'].widget.attrs['class'] = 'form-control'
        self.fields['data_nascimento'].widget.attrs['placeholder'] = 'Digite sua data de nascimento'
        self.fields['cpf'].widget.attrs['class'] = 'form-control'
        self.fields['cpf'].widget.attrs['placeholder'] = 'Digite seu CPF'
        self.fields['rg'].widget.attrs['class'] = 'form-control'
        self.fields['rg'].widget.attrs['placeholder'] = 'Digite seu RG'
        self.fields['orgaoemissor'].widget.attrs['class'] = 'form-control'
        self.fields['orgaoemissor'].widget.attrs['placeholder'] = 'Digite seu Orgao Emissor'
        self.fields['foto'].widget.attrs['class'] = 'form-control'
        self.fields['foto'].widget.attrs['placeholder'] = 'Escolha uma foto'
        self.fields['id_endereco'].widget.attrs['class'] = 'form-control'
        self.fields['id_endereco'].widget.attrs['placeholder'] = 'Escolha seu endereco'
        

    def save(self, commit=True):
        # Verifique se a senha fornecida esta no formato hash
        user = super(ProfileForm, self).save(commit=False)
        if commit:
            user.save()
        return user



class UserRegisterForm(forms.ModelForm):
    repetir_password = forms.CharField(label='Confirmação de Senha', widget=forms.PasswordInput, required=True)
    
    cep = forms.CharField(label='CEP:', max_length=10)
    rua = forms.CharField(label='Rua:', max_length=100)
    bairro = forms.CharField(label='Bairro:', max_length=45)
    cidade = forms.CharField(label='Cidade:', max_length=20)
    estado = forms.CharField(label='Estado:', max_length=2)
    pais = forms.CharField(label='País:', max_length=45)
   
    numero = forms.IntegerField(label='Numero:', required=False)
    complemento = forms.CharField(label='Complemento:', max_length=45,required=False)
    pontoreferencia = forms.CharField(label='Ponto de referência:', max_length=45, widget=forms.Textarea, required=False)

    class Meta:
        model = Usuario
        fields = '__all__'
    

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs['class'] = 'form-control'
        self.fields['nome'].widget.attrs['placeholder'] = 'Digite o nome'
        self.fields['nome'].required = True
        self.fields['sobrenome'].widget.attrs['class'] = 'form-control'
        self.fields['sobrenome'].widget.attrs['placeholder'] = 'Digite o sobrenome'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Digite o email'
        self.fields['email'].required = True
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Digite uma senha'
        self.fields['repetir_password'].widget.attrs['class'] = 'form-control'
        self.fields['repetir_password'].widget.attrs['placeholder'] = 'Repita a senha'
        self.fields['id_tipo_usuario'].widget.attrs['class'] = 'form-control'
        self.fields['id_tipo_usuario'].queryset = TipoUsuario.objects.all()
        self.fields['id_genero'].widget.attrs['class'] = 'form-control'
        self.fields['id_genero'].queryset = Genero.objects.all()
        self.fields['data_nascimento'].widget.attrs['class'] = 'form-control'
        self.fields['data_nascimento'].widget.attrs['placeholder'] = 'Digite a data de nascimento'
        self.fields['cpf'].widget.attrs['class'] = 'form-control'
        self.fields['cpf'].widget.attrs['placeholder'] = 'Digite o CPF'
        self.fields['cpf'].widget.attrs['onblur'] = 'validar_cpf(this.value)'
        self.fields['cpf'].required = True
        self.fields['rg'].widget.attrs['class'] = 'form-control'
        self.fields['rg'].widget.attrs['placeholder'] = 'Digite o RG'
        self.fields['rg'].required = True
        self.fields['rg'].label = "RG ou Matricula de Certidão de Nascimento"
        self.fields['orgaoemissor'].widget.attrs['class'] = 'form-control'
        self.fields['orgaoemissor'].widget.attrs['placeholder'] = 'Digite o Orgao Emissor'
        self.fields['orgaoemissor'].required = True
        self.fields['foto'].widget.attrs['class'] = 'form-control'
        self.fields['foto'].widget.attrs['placeholder'] = 'Escolha uma foto'

       
        self.fields['cep'].widget.attrs['class'] = 'form-control'
        self.fields['cep'].widget.attrs['placeholder'] = 'Digite o CEP'
        self.fields['rua'].widget.attrs['class'] = 'form-control'
        self.fields['rua'].widget.attrs['placeholder'] = 'Digite a rua'
        self.fields['bairro'].widget.attrs['class'] = 'form-control'
        self.fields['bairro'].widget.attrs['placeholder'] = 'Digite o bairro'
        self.fields['cidade'].widget.attrs['class'] = 'form-control'
        self.fields['cidade'].widget.attrs['placeholder'] = 'Digite a cidade'
        self.fields['estado'].widget.attrs['class'] = 'form-control'
        self.fields['estado'].widget.attrs['placeholder'] = 'Digite o estado'
        self.fields['pais'].widget.attrs['class'] = 'form-control'
        self.fields['pais'].widget.attrs['placeholder'] = 'Digite o pais'

        self.fields['numero'].widget.attrs['class'] = 'form-control'
        self.fields['numero'].widget.attrs['placeholder'] = 'Digite o numero'
        self.fields['complemento'].widget.attrs['class'] = 'form-control'
        self.fields['complemento'].widget.attrs['placeholder'] = 'Digite o complemento'
        self.fields['pontoreferencia'].widget.attrs['class'] = 'form-control'
        self.fields['pontoreferencia'].widget.attrs['placeholder'] = 'Digite um ponto de referência'

        self.fields['cep'].required = False
        self.fields['rua'].required = False
        self.fields['bairro'].required = False
        self.fields['bairro'].required = False
        self.fields['cidade'].required = False
        self.fields['estado'].required = False
        self.fields['pais'].required = False
        self.fields['numero'].required = False
        self.fields['complemento'].required = False
        self.fields['pontoreferencia'].required = False

    def clean(self):
        cleaned_data = super(UserRegisterForm, self).clean()

        cep = cleaned_data.get("cep")
        rua = cleaned_data.get("rua")
        bairro = cleaned_data.get("bairro")
        cidade = cleaned_data.get("cidade")
        estado = cleaned_data.get("estado")
        pais = cleaned_data.get("pais")
        numero = cleaned_data.get("numero")

        msg = "Este campo é obrigatório."
        if cep:
            if not rua:
                self.add_error('rua', msg)
            if not bairro:
                self.add_error('bairro', msg)
            if not cidade:
                self.add_error('cidade', msg)
            if not estado:
                self.add_error('estado', msg)
            if not pais:
                self.add_error('pais', msg)
            if not numero:
                self.add_error('numero', msg)
        elif rua:
            if not rua:
                self.add_error('rua', msg)
            if not bairro:
                self.add_error('bairro', msg)
            if not cidade:
                self.add_error('cidade', msg)
            if not estado:
                self.add_error('estado', msg)
            if not pais:
                self.add_error('pais', msg)
            if not numero:
                self.add_error('numero', msg)
        elif bairro:
            if not cep:
                self.add_error('cep', msg)
            if not rua:
                self.add_error('rua', msg)
            if not cidade:
                self.add_error('cidade', msg)
            if not estado:
                self.add_error('estado', msg)
            if not pais:
                self.add_error('pais', msg)
            if not numero:
                self.add_error('numero', msg)
        elif cidade:
            if not cep:
                self.add_error('cep', msg)
            if not rua:
                self.add_error('rua', msg)
            if not bairro:
                self.add_error('bairro', msg)
            if not estado:
                self.add_error('estado', msg)
            if not pais:
                self.add_error('pais', msg)
            if not numero:
                self.add_error('numero', msg)
        elif estado:
            if not cep:
                self.add_error('cep', msg)
            if not rua:
                self.add_error('rua', msg)
            if not bairro:
                self.add_error('bairro', msg)
            if not cidade:
                self.add_error('cidade', msg)
            if not pais:
                self.add_error('pais', msg)
            if not numero:
                self.add_error('numero', msg)
        elif pais:
            if not cep:
                self.add_error('cep', msg)
            if not rua:
                self.add_error('rua', msg)
            if not bairro:
                self.add_error('bairro', msg)
            if not cidade:
                self.add_error('cidade', msg)
            if not estado:
                self.add_error('estado', msg)
            if not numero:
                self.add_error('numero', msg)
        elif numero:
            if not cep:
                self.add_error('cep', msg)
            if not rua:
                self.add_error('rua', msg)
            if not bairro:
                self.add_error('bairro', msg)
            if not cidade:
                self.add_error('cidade', msg)
            if not estado:
                self.add_error('estado', msg)
            if not pais:
                self.add_error('pais', msg)


class CompanyRegisterForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'

    cep = forms.CharField(label='CEP:', max_length=10)
    rua = forms.CharField(label='Rua:', max_length=100)
    bairro = forms.CharField(label='Bairro:', max_length=45)
    cidade = forms.CharField(label='Cidade:', max_length=20)
    estado = forms.CharField(label='Estado:', max_length=2)
    pais = forms.CharField(label='País:', max_length=45)

    numeroed = forms.IntegerField(label='Numero:')
    complemento = forms.CharField(label='Complemento:', max_length=45)
    pontoreferencia = forms.CharField(label='Ponto de referência:', max_length=45, widget=forms.Textarea)

    
    def __init__(self, *args, **kwargs):
        super(CompanyRegisterForm, self).__init__(*args, **kwargs)
        self.fields['razaosocial'].widget.attrs['class'] = 'form-control'
        self.fields['razaosocial'].widget.attrs['placeholder'] = 'Digite a Razão Social'
        self.fields['nomefantasia'].widget.attrs['class'] = 'form-control'
        self.fields['nomefantasia'].widget.attrs['placeholder'] = 'Digite o Nome Fantasia'
        self.fields['cnpj'].widget.attrs['class'] = 'form-control'
        self.fields['cnpj'].widget.attrs['onblur'] = 'get_cnpj_data(this.value)'
        self.fields['cnpj'].widget.attrs['placeholder'] = 'Digite a Razão Social'
        self.fields['ie'].widget.attrs['class'] = 'form-control'
        self.fields['ie'].widget.attrs['placeholder'] = 'Inscrição Estadual'
        self.fields['id_tipo_empresa'].widget.attrs['class'] = 'form-control'
        self.fields['id_tipo_empresa'].queryset = TipoEmpresa.objects.all()
       
        self.fields['cep'].widget.attrs['class'] = 'form-control'
        self.fields['cep'].widget.attrs['onblur'] = 'get_cep_data(this.value)'
        self.fields['cep'].widget.attrs['placeholder'] = 'Digite o CEP'
        self.fields['rua'].widget.attrs['class'] = 'form-control'
        self.fields['rua'].widget.attrs['placeholder'] = 'Digite a rua'
        self.fields['bairro'].widget.attrs['class'] = 'form-control'
        self.fields['bairro'].widget.attrs['placeholder'] = 'Digite o bairro'
        self.fields['cidade'].widget.attrs['class'] = 'form-control'
        self.fields['cidade'].widget.attrs['placeholder'] = 'Digite a cidade'
        self.fields['estado'].widget.attrs['class'] = 'form-control'
        self.fields['estado'].widget.attrs['placeholder'] = 'Digite o estado'
        self.fields['pais'].widget.attrs['class'] = 'form-control'
        self.fields['pais'].widget.attrs['placeholder'] = 'Digite o pais'

        self.fields['numeroed'].widget.attrs['class'] = 'form-control'
        self.fields['numeroed'].widget.attrs['placeholder'] = 'Digite o numero'
        self.fields['complemento'].widget.attrs['class'] = 'form-control'
        self.fields['complemento'].widget.attrs['placeholder'] = 'Digite o complemento'
        self.fields['pontoreferencia'].widget.attrs['class'] = 'form-control'
        self.fields['pontoreferencia'].widget.attrs['placeholder'] = 'Digite um ponto de referência'
        

        self.fields['razaosocial'].required = False
        self.fields['nomefantasia'].required = True
        self.fields['cnpj'].required = False
        self.fields['ie'].required = False
        self.fields['id_tipo_empresa'].required = False


        self.fields['cep'].required = False
        self.fields['rua'].required = False
        self.fields['bairro'].required = False
        self.fields['bairro'].required = False
        self.fields['cidade'].required = False
        self.fields['estado'].required = False
        self.fields['pais'].required = False
        self.fields['numeroed'].required = False
        self.fields['complemento'].required = False
        self.fields['pontoreferencia'].required = False
        
    def clean(self):
        cleaned_data = super(CompanyRegisterForm, self).clean()

        cep = cleaned_data.get("cep")
        rua = cleaned_data.get("rua")
        bairro = cleaned_data.get("bairro")
        cidade = cleaned_data.get("cidade")
        estado = cleaned_data.get("estado")
        pais = cleaned_data.get("pais")
        numero = cleaned_data.get("numeroed")

        msg = "This field is required."
        if cep:
            if not rua:
                self.add_error('rua', msg)
            if not bairro:
                self.add_error('bairro', msg)
            if not cidade:
                self.add_error('cidade', msg)
            if not estado:
                self.add_error('estado', msg)
            if not pais:
                self.add_error('pais', msg)
            if not numero:
                self.add_error('numeroed', msg)
        elif rua:
            if not rua:
                self.add_error('rua', msg)
            if not bairro:
                self.add_error('bairro', msg)
            if not cidade:
                self.add_error('cidade', msg)
            if not estado:
                self.add_error('estado', msg)
            if not pais:
                self.add_error('pais', msg)
            if not numero:
                self.add_error('numeroed', msg)
        elif bairro:
            if not cep:
                self.add_error('cep', msg)
            if not rua:
                self.add_error('rua', msg)
            if not cidade:
                self.add_error('cidade', msg)
            if not estado:
                self.add_error('estado', msg)
            if not pais:
                self.add_error('pais', msg)
            if not numero:
                self.add_error('numeroed', msg)
        elif cidade:
            if not cep:
                self.add_error('cep', msg)
            if not rua:
                self.add_error('rua', msg)
            if not bairro:
                self.add_error('bairro', msg)
            if not estado:
                self.add_error('estado', msg)
            if not pais:
                self.add_error('pais', msg)
            if not numero:
                self.add_error('numeroed', msg)
        elif estado:
            if not cep:
                self.add_error('cep', msg)
            if not rua:
                self.add_error('rua', msg)
            if not bairro:
                self.add_error('bairro', msg)
            if not cidade:
                self.add_error('cidade', msg)
            if not pais:
                self.add_error('pais', msg)
            if not numero:
                self.add_error('numeroed', msg)
        elif pais:
            if not cep:
                self.add_error('cep', msg)
            if not rua:
                self.add_error('rua', msg)
            if not bairro:
                self.add_error('bairro', msg)
            if not cidade:
                self.add_error('cidade', msg)
            if not estado:
                self.add_error('estado', msg)
            if not numero:
                self.add_error('numeroed', msg)
        elif numero:
            if not cep:
                self.add_error('cep', msg)
            if not rua:
                self.add_error('rua', msg)
            if not bairro:
                self.add_error('bairro', msg)
            if not cidade:
                self.add_error('cidade', msg)
            if not estado:
                self.add_error('estado', msg)
            if not pais:
                self.add_error('pais', msg)


class PhoneForm(forms.Form):
    tipo_telefone = forms.ModelChoiceField (TipoTelefone, label='Tipo de Telefone:', widget=forms.Select(), required=False)
    numero = forms.CharField(label='Numero:', max_length=15)
    ramal = forms.CharField(label='Ramal:', max_length=4, required=False)
    nome_contato = forms.CharField(label='Contato:', max_length=45, required=False)

    def __init__(self, *args, **kwargs):
        super(PhoneForm, self).__init__(*args, **kwargs)
        self.fields['tipo_telefone'].widget.attrs['class'] = 'form-control'
        self.fields['tipo_telefone'].queryset = TipoTelefone.objects.all()
        self.fields['numero'].widget.attrs['class'] = 'form-control celphones'
        self.fields['numero'].widget.attrs['placeholder'] = 'numero'
        self.fields['ramal'].widget.attrs['class'] = 'form-control'
        self.fields['ramal'].widget.attrs['placeholder'] = 'ramal'
        self.fields['nome_contato'].widget.attrs['class'] = 'form-control'
        self.fields['nome_contato'].widget.attrs['placeholder'] = 'nome do contato'
