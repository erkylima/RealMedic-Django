from django import forms
from django.contrib.auth.models import User

from core.models import Atendente
from core.util.labels_property import LabesProperty
from core.util.util_manager import adiciona_form_control


class AtendenteForm(forms.ModelForm):
    # password = forms.CharField(label="Senha",
    #                            widget=forms.PasswordInput(
    #                                attrs={"id": "password", }), )
    # confirmpassword = forms.CharField(label="Confirme Senha",
    #                                   widget=forms.PasswordInput(
    #                                       attrs={"id": "confirmpassword", }), )

    class Meta:
        model = Atendente
        fields = '__all__'
        exclude = ('senha', 'user')

    def __init__(self, *args, **kwargs):
        super(AtendenteForm, self).__init__(*args, **kwargs)
        adiciona_form_control(self)

    def clean(self):
        instancia = self.instance
        print('clean')
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
