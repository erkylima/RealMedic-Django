from django import forms
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from core.models import Atendente
from core.modulos.departamento.departamento import Departamento
from core.modulos.empresa.empresa import Empresa
from core.util.labels_property import LabesProperty
from core.util.util_manager import adiciona_form_control


class AtendenteForm(forms.ModelForm):
    class Meta:
        model = Atendente
        fields = '__all__'
        exclude = ('senha', 'user')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(AtendenteForm, self).__init__(*args, **kwargs)
        instancia = self.instance

        self.fields['departamento'].queryset = Departamento.objects.filter(empresa_id=self.user.userProfile.empresa_id)
        self.fields['perfil'].initial = 2 # Atendente id 2
        if self.instance.pk:
            self.fields['departamento'].queryset = Departamento.objects.filter(empresa=instancia.departamento.empresa)

        self.fields['departamento'].required = False

        adiciona_form_control(self)

    def clean(self):
        instancia = self.instance
        print('clean')
        print(self.cleaned_data)
        login = self.cleaned_data.get('usuario', None)
        email = self.cleaned_data.get('email', None)
        if instancia is None:
            self.validarLoginUsuario(login)
            self.validarEmailUsuario(email)
        else:
            if instancia.usuario != login:
                self.validarLoginUsuario(login)
            if instancia.email != email:
                self.validarEmailUsuario(email)

    def validarLoginUsuario(self, login):
        usuario = Atendente.objects.filter(usuario=login)
        user = User.objects.filter(username=login)
        if usuario.exists() or user.exists():
            self.add_error('usuario', LabesProperty.ERROR_NOME_USUARIO_EXISTE)

    def validarEmailUsuario(self, email):
        email = Atendente.objects.filter(email=email)
        if email.exists():
            self.add_error('email', LabesProperty.ERROR_EMAIL_USUARIO_EXISTE)
