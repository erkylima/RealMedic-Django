from django import forms
from django.contrib.auth.models import User
from core.models import Atendente
from core.modulos.departamento.departamento import Departamento
from core.modulos.user_profile.user_profile import UserProfile
from core.util.labels_property import LabesProperty
from core.util.util_manager import adiciona_form_control, get_user_type


class AtendenteForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ('senha', 'user','perfil')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(AtendenteForm, self).__init__(*args, **kwargs)
        instancia = self.instance
        usuario = get_user_type(self.user)
        self.fields['departamento'].queryset = Departamento.objects.filter(empresa_id=usuario.userProfile.departamento.empresa_id)
        # self.fields['perfil'].initial = Group.objects.get(name='Atendente').pk # Pegar id do grupo de permissão Atendente
        if self.instance.pk:
            self.fields['departamento'].queryset = Departamento.objects.filter(empresa=usuario.userProfile.departamento.empresa)
            self.fields['departamento'].initial = instancia.userProfile.departamento
            self.fields['nome'].initial = instancia.userProfile.nome
            self.fields['usuario'].initial = instancia.userProfile.usuario
            self.fields['email'].initial = instancia.userProfile.email


        self.fields['departamento'].required = False

        adiciona_form_control(self)

    def clean(self):
        instancia = self.instance
        print('clean')
        # print(self.cleaned_data)
        login = self.cleaned_data.get('usuario', None)
        email = self.cleaned_data.get('email', None)

        if instancia is None:
            self.validarLoginUsuario(login)
            self.validarEmailUsuario(email)
        else:
            if type(instancia) == type(UserProfile):
                if instancia.usuario != login:
                    self.validarLoginUsuario(login)
                if instancia.email != email:
                    self.validarEmailUsuario(email)
            else:
                if instancia.userProfile.usuario != login:
                    self.validarLoginUsuario(login)
                if instancia.userProfile.email != email:
                    self.validarEmailUsuario(email)

    def validarLoginUsuario(self, login):
        usuario = Atendente.objects.filter(userProfile__usuario=login)
        user = User.objects.filter(username=login)
        if usuario.exists() or user.exists():
            self.add_error('usuario', LabesProperty.ERROR_NOME_USUARIO_EXISTE)

    def validarEmailUsuario(self, email):
        email = Atendente.objects.filter(userProfile__email=email)
        if email.exists():
            self.add_error('email', LabesProperty.ERROR_EMAIL_USUARIO_EXISTE)
