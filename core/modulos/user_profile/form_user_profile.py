from django import forms
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from core.models import Empresa, UserProfile
from core.modulos.departamento.departamento import Departamento
from core.util.labels_property import LabesProperty
from core.util.util_manager import adiciona_form_control


class UserProfileForm(forms.ModelForm):
    # password = forms.CharField(label="Senha",
    #                            widget=forms.PasswordInput(
    #                                attrs={"id": "password", }), )
    # confirmpassword = forms.CharField(label="Confirme Senha",
    #                                   widget=forms.PasswordInput(
    #                                       attrs={"id": "confirmpassword", }), )

    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ('senha', 'user')

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        select_master_empresa = 'empresa'

        self.fields['empresa'].widget.attrs['id'] = 'id_empresa'
        self.fields['empresa'].widget.attrs[
            'onchange'] = 'carregarElementoPorIdFK("' + reverse_lazy(
            "core:modulo:departamento:getDepartamentosPorIdEmpresa",
            kwargs={'idEmpresa': '00'}).__str__() + f'","id_empresa","id_departamento","{select_master_empresa}")'
        departamentos = Departamento.objects.none()

        self.fields['departamento'].queryset = departamentos

        self.fields['perfil'].initial = UserProfile.objects.get(nome='Gerenciador').pk # Pegar id do grupo de permissão Gerente
        if select_master_empresa in self.data:
            try:
                empresa_id = int(self.data.get('empresa'))
                print(empresa_id)
                self.fields['departamento'].queryset = Departamento.objects.filter(
                    empresa_id=empresa_id)
                print(self.fields['departamento'].queryset)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['departamento'].queryset = Departamento.objects.filter(
                empresa_id=self.instance.departamento.empresa_id)
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
        usuario = UserProfile.objects.filter(usuario=login)
        user = User.objects.filter(username=login)
        if usuario.exists() or user.exists():
            self.add_error('usuario', LabesProperty.ERROR_NOME_USUARIO_EXISTE)

    def validarEmailUsuario(self, email):
        email = UserProfile.objects.filter(email=email)
        if email.exists():
            self.add_error('email', LabesProperty.ERROR_EMAIL_USUARIO_EXISTE)
