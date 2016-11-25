#-*- coding: utf-8 -*-


##################################################
#               DJANGO IMPORTS                   #
##################################################
from django import forms
from django.conf import settings
from django.contrib.auth.forms import ReadOnlyPasswordHashField

##################################################


##################################################
#               CUSTOM IMPORTS                   #
##################################################
from .models import Usuario, Genero, TipoUsuario, TipoEmpresa, TipoTelefone, TelefoneEmpresa # MODELS
##################################################


'''
---------------------------------------
            ADMIN AREA
---------------------------------------
'''

class UserCreationForm(forms.ModelForm):
    # Formulario para criacao de novos usuarios.Inclui todos os campos requeridos.
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('email',)

    def clean_password2(self):
        # Verifique se as duas entradas de senha correspondem
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Verifique se a senha fornecida esta no formato hash
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """Um formulario para atualizar os usuarios . Inclui todos os campos
    de um usuario, mas substitui o campo de senha com administracao de
    hash de senha.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Usuario
        fields = ('email', 'password', 'is_active', 'is_admin')

    def clean_password(self):
        # Retorna o valor inicial caso nao tenha acesso
        return self.initial["password"]

'''
---------------------------------------
            END ADMIN AREA
---------------------------------------
'''



'''
---------------------------------------
            AUTH FORMS
---------------------------------------
'''

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email:', max_length=75)
    password = forms.CharField(label='Senha:', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        # Email Fields widget
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Digite seu email'

        # Password Fields widget
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
        # Nome Fields widget
        self.fields['nome'].widget.attrs['class'] = 'form-control'
        self.fields['nome'].widget.attrs['placeholder'] = 'Digite seu nome'

        # Sobrenome Fields widget
        self.fields['sobrenome'].widget.attrs['class'] = 'form-control'
        self.fields['sobrenome'].widget.attrs['placeholder'] = 'Digite seu sobrenome'

        # Email Fields widget
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Digite seu email'

        # Password Fields widget
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Digite sua senha'
        pass

'''
---------------------------------------
            END AUTH FORMS
---------------------------------------
'''



'''
---------------------------------------
            PROFILE FORMS
---------------------------------------
'''

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('nome','sobrenome','nomecompleto','id_tipo_usuario','id_endereco','id_genero','cpf','data_nascimento','rg','orgaoemissor','foto')

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        # Nome Fields widget
        self.fields['nome'].widget.attrs['class'] = 'form-control'
        self.fields['nome'].widget.attrs['placeholder'] = 'Digite seu nome'

        # Sobrenome Fields widget
        self.fields['sobrenome'].widget.attrs['class'] = 'form-control'
        self.fields['sobrenome'].widget.attrs['placeholder'] = 'Digite seu sobrenome'

        # Nome Completo Fields widget
        self.fields['nomecompleto'].widget.attrs['class'] = 'form-control'
        self.fields['nomecompleto'].widget.attrs['placeholder'] = 'Digite seu nome completo'

        # Genero Fields widget
        self.fields['id_genero'].widget.attrs['class'] = 'form-control'
        self.fields['id_genero'].widget.attrs['placeholder'] = 'Escolha seu genero'

        # Data Nascimento Fields widget
        self.fields['data_nascimento'].widget.attrs['class'] = 'form-control'
        self.fields['data_nascimento'].widget.attrs['placeholder'] = 'Digite sua data de nascimento'

        # CPF Fields widget
        self.fields['cpf'].widget.attrs['class'] = 'form-control'
        self.fields['cpf'].widget.attrs['placeholder'] = 'Digite seu CPF'

        # RG Fields widget
        self.fields['rg'].widget.attrs['class'] = 'form-control'
        self.fields['rg'].widget.attrs['placeholder'] = 'Digite seu RG'

        # Orgao Emissor Fields widget
        self.fields['orgaoemissor'].widget.attrs['class'] = 'form-control'
        self.fields['orgaoemissor'].widget.attrs['placeholder'] = 'Digite seu Orgao Emissor'

        # Foto Fields widget
        self.fields['foto'].widget.attrs['class'] = 'form-control'
        self.fields['foto'].widget.attrs['placeholder'] = 'Escolha uma foto'

        # Foto Fields widget
        self.fields['id_endereco'].widget.attrs['class'] = 'form-control'
        self.fields['id_endereco'].widget.attrs['placeholder'] = 'Escolha seu endereco'
        

    def save(self, commit=True):
        # Verifique se a senha fornecida esta no formato hash
        user = super(ProfileForm, self).save(commit=False)
        if commit:
            user.save()
        return user

'''
---------------------------------------
            END PROFILE FORMS
---------------------------------------
'''



'''
---------------------------------------
            USER FORMS
---------------------------------------
'''

class UserRegisterForm(forms.Form):

    # FIELDS USUARIO
    nome = forms.CharField(label='Nome:', max_length=45)
    sobrenome = forms.CharField(label='Sobrenome:', max_length=45, required=False)
    email = forms.CharField(label='Email:', max_length=75)
    password = forms.CharField(label='Senha', widget=forms.PasswordInput, required=False)
    repetir_password = forms.CharField(label='Confirmação de Senha', widget=forms.PasswordInput, required=False)
    tipo_usuario = forms.ModelChoiceField (TipoUsuario, label='Tipo de Usuário:', widget=forms.Select())
    genero = forms.ModelChoiceField(Genero, label='Genero:', widget=forms.Select())
    data_nascimento = forms.DateField(label='Data de Nascimento:',input_formats=settings.DATE_INPUT_FORMATS, required=False)
    cpf = forms.CharField(label='CPF:', max_length=14)
    rg = forms.CharField(label='RG:', max_length=12)
    orgaoemissor = forms.CharField(label='Orgão Emissor:', max_length=45)
    foto = forms.ImageField(label='Foto:', required=False)

    # FIELDS LOGRADOURO
    cep = forms.CharField(label='CEP:', max_length=10)
    rua = forms.CharField(label='Rua:', max_length=100)
    bairro = forms.CharField(label='Bairro:', max_length=45)
    cidade = forms.CharField(label='Cidade:', max_length=20)
    estado = forms.CharField(label='Estado:', max_length=2)
    pais = forms.CharField(label='País:', max_length=45)

    # FIELDS ENDERECO
    numero = forms.IntegerField(label='Numero:', required=False)
    complemento = forms.CharField(label='Complemento:', max_length=45,required=False)
    pontoreferencia = forms.CharField(label='Ponto de referência:', max_length=45, widget=forms.Textarea, required=False)


    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        '''
            FIELDS USUARIO
        '''

        # Frist Name Fields widget
        self.fields['nome'].widget.attrs['class'] = 'form-control'
        self.fields['nome'].widget.attrs['placeholder'] = 'Digite o nome'

        # Last Name Fields widget
        self.fields['sobrenome'].widget.attrs['class'] = 'form-control'
        self.fields['sobrenome'].widget.attrs['placeholder'] = 'Digite o sobrenome'

        # Email Fields widget
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Digite o email'

        # Password Fields widget
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Digite uma senha'

        # Repetir_senha Fields widget
        self.fields['repetir_password'].widget.attrs['class'] = 'form-control'
        self.fields['repetir_password'].widget.attrs['placeholder'] = 'Repita a senha'

        # Tipo_usuario Fields widget
        self.fields['tipo_usuario'].widget.attrs['class'] = 'form-control'
        self.fields['tipo_usuario'].queryset = TipoUsuario.objects.all()

        # Genero Fields widget
        self.fields['genero'].widget.attrs['class'] = 'form-control'
        self.fields['genero'].queryset = Genero.objects.all()

        # Data Nascimento Fields widget
        self.fields['data_nascimento'].widget.attrs['class'] = 'form-control'
        self.fields['data_nascimento'].widget.attrs['placeholder'] = 'Digite a data de nascimento'

        # CPF Fields widget
        self.fields['cpf'].widget.attrs['class'] = 'form-control'
        self.fields['cpf'].widget.attrs['placeholder'] = 'Digite o CPF'
        self.fields['cpf'].widget.attrs['onblur'] = 'validar_cpf(this.value)'

        # RG Fields widget
        self.fields['rg'].widget.attrs['class'] = 'form-control'
        self.fields['rg'].widget.attrs['placeholder'] = 'Digite o RG'

        # Orgao Emissor Fields widget
        self.fields['orgaoemissor'].widget.attrs['class'] = 'form-control'
        self.fields['orgaoemissor'].widget.attrs['placeholder'] = 'Digite o Orgao Emissor'

        # Foto Fields widget
        self.fields['foto'].widget.attrs['class'] = 'form-control'
        self.fields['foto'].widget.attrs['placeholder'] = 'Escolha uma foto'


        '''
            FIELDS LOGRADOURO
        '''

        # CEP Fields widget
        self.fields['cep'].widget.attrs['class'] = 'form-control'
        self.fields['cep'].widget.attrs['onblur'] = 'get_cep_data(this.value)'
        self.fields['cep'].widget.attrs['placeholder'] = 'Digite o CEP'

        # Rua Fields widget
        self.fields['rua'].widget.attrs['class'] = 'form-control'
        self.fields['rua'].widget.attrs['placeholder'] = 'Digite a rua'

        # Bairro Fields widget
        self.fields['bairro'].widget.attrs['class'] = 'form-control'
        self.fields['bairro'].widget.attrs['placeholder'] = 'Digite o bairro'

        # Cidade Fields widget
        self.fields['cidade'].widget.attrs['class'] = 'form-control'
        self.fields['cidade'].widget.attrs['placeholder'] = 'Digite a cidade'

        # Estado Fields widget
        self.fields['estado'].widget.attrs['class'] = 'form-control'
        self.fields['estado'].widget.attrs['placeholder'] = 'Digite o estado'

        # Pais Fields widget
        self.fields['pais'].widget.attrs['class'] = 'form-control'
        self.fields['pais'].widget.attrs['placeholder'] = 'Digite o pais'


        '''
            FIELDS ENDERECO
        '''

        # Numero Fields widget
        self.fields['numero'].widget.attrs['class'] = 'form-control'
        self.fields['numero'].widget.attrs['placeholder'] = 'Digite o numero'

        # Complemento Fields widget
        self.fields['complemento'].widget.attrs['class'] = 'form-control'
        self.fields['complemento'].widget.attrs['placeholder'] = 'Digite o complemento'

        # Pontoreferencia Fields widget
        self.fields['pontoreferencia'].widget.attrs['class'] = 'form-control'
        self.fields['pontoreferencia'].widget.attrs['placeholder'] = 'Digite um ponto de referência'

        pass

'''
---------------------------------------
            END USER FORMS
---------------------------------------
'''



'''
---------------------------------------
            COMPANY FORMS
---------------------------------------
'''

class CompanyRegisterForm(forms.Form):

    # FIELDS EMPRESA
    razaosocial = forms.CharField(label='Razão Social:', max_length=100)
    nomefantasia = forms.CharField(label='Nome Fantasia:', max_length=100)
    cnpj = forms.CharField(label='CNPJ:', max_length=20)
    ie = forms.CharField(label='Inscrição Estadual', max_length=45)
    tipo_empresa = forms.ModelChoiceField (TipoEmpresa, label='Tipo de Empresa:', widget=forms.Select())

    # FIELDS LOGRADOURO
    cep = forms.CharField(label='CEP:', max_length=10)
    rua = forms.CharField(label='Rua:', max_length=100)
    bairro = forms.CharField(label='Bairro:', max_length=45)
    cidade = forms.CharField(label='Cidade:', max_length=20)
    estado = forms.CharField(label='Estado:', max_length=2)
    pais = forms.CharField(label='País:', max_length=45)

    # FIELDS ENDERECO
    numeroed = forms.IntegerField(label='Numero:')
    complemento = forms.CharField(label='Complemento:', max_length=45)
    pontoreferencia = forms.CharField(label='Ponto de referência:', max_length=45, widget=forms.Textarea)

    
    def __init__(self, *args, **kwargs):
        super(CompanyRegisterForm, self).__init__(*args, **kwargs)

        '''
            FIELDS EMPRESA
        '''

        # Razaosocial Fields widget
        self.fields['razaosocial'].widget.attrs['class'] = 'form-control'
        self.fields['razaosocial'].widget.attrs['placeholder'] = 'Digite a Razão Social'

        # Nomefantasia Fields widget
        self.fields['nomefantasia'].widget.attrs['class'] = 'form-control'
        self.fields['nomefantasia'].widget.attrs['placeholder'] = 'Digite o Nome Fantasia'

        # Cnpj Fields widget
        self.fields['cnpj'].widget.attrs['class'] = 'form-control'
        self.fields['cnpj'].widget.attrs['onblur'] = 'get_cnpj_data(this.value)'
        self.fields['cnpj'].widget.attrs['placeholder'] = 'Digite a Razão Social'


        # Ie Fields widget
        self.fields['ie'].widget.attrs['class'] = 'form-control'
        self.fields['ie'].widget.attrs['placeholder'] = 'Inscrição Estadual'

        # Tipo_empresa Fields widget
        self.fields['tipo_empresa'].widget.attrs['class'] = 'form-control'
        self.fields['tipo_empresa'].queryset = TipoEmpresa.objects.all()


        '''
            FIELDS LOGRADOURO
        '''

        # CEP Fields widget
        self.fields['cep'].widget.attrs['class'] = 'form-control'
        self.fields['cep'].widget.attrs['onblur'] = 'get_cep_data(this.value)'
        self.fields['cep'].widget.attrs['placeholder'] = 'Digite o CEP'

        # Rua Fields widget
        self.fields['rua'].widget.attrs['class'] = 'form-control'
        self.fields['rua'].widget.attrs['placeholder'] = 'Digite a rua'

        # Bairro Fields widget
        self.fields['bairro'].widget.attrs['class'] = 'form-control'
        self.fields['bairro'].widget.attrs['placeholder'] = 'Digite o bairro'

        # Cidade Fields widget
        self.fields['cidade'].widget.attrs['class'] = 'form-control'
        self.fields['cidade'].widget.attrs['placeholder'] = 'Digite a cidade'

        # Estado Fields widget
        self.fields['estado'].widget.attrs['class'] = 'form-control'
        self.fields['estado'].widget.attrs['placeholder'] = 'Digite o estado'

        # Pais Fields widget
        self.fields['pais'].widget.attrs['class'] = 'form-control'
        self.fields['pais'].widget.attrs['placeholder'] = 'Digite o pais'


        '''
            FIELDS ENDERECO
        '''

        # Numero Fields widget
        self.fields['numeroed'].widget.attrs['class'] = 'form-control'
        self.fields['numeroed'].widget.attrs['placeholder'] = 'Digite o numero'

        # Complemento Fields widget
        self.fields['complemento'].widget.attrs['class'] = 'form-control'
        self.fields['complemento'].widget.attrs['placeholder'] = 'Digite o complemento'

        # Pontoreferencia Fields widget
        self.fields['pontoreferencia'].widget.attrs['class'] = 'form-control'
        self.fields['pontoreferencia'].widget.attrs['placeholder'] = 'Digite um ponto de referência'
        
        pass

'''
---------------------------------------
            END COMPANY FORMS
---------------------------------------
'''



'''
---------------------------------------
            PHONE FORMS
---------------------------------------
'''

class PhoneForm(forms.Form):

    # FIEDS TELEFONE
    tipo_telefone = forms.ModelChoiceField (TipoTelefone, label='Tipo de Telefone:', widget=forms.Select())
    numero = forms.CharField(label='Numero:', max_length=15)
    ramal = forms.CharField(label='Ramal:', max_length=4, required=False)
    nome_contato = forms.CharField(label='Contato:', max_length=45, required=False)

    def __init__(self, *args, **kwargs):
        super(PhoneForm, self).__init__(*args, **kwargs)

        '''
            FIELDS TELEFONE
        '''

        # Tipotelefone Fields widget
        self.fields['tipo_telefone'].widget.attrs['class'] = 'form-control'
        self.fields['tipo_telefone'].queryset = TipoTelefone.objects.all()

        # Numero Fields widget
        self.fields['numero'].widget.attrs['class'] = 'form-control'
        self.fields['numero'].widget.attrs['placeholder'] = 'numero'

        # Ramal Fields widget
        self.fields['ramal'].widget.attrs['class'] = 'form-control'
        self.fields['ramal'].widget.attrs['placeholder'] = 'ramal'

        # Nomecontato Fields widget
        self.fields['nome_contato'].widget.attrs['class'] = 'form-control'
        self.fields['nome_contato'].widget.attrs['placeholder'] = 'nome do contato'

'''
---------------------------------------
            END PHONE FORMS
---------------------------------------
'''