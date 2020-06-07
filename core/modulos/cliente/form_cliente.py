from django import forms
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from core.models import Cliente
from core.modulos.departamento.departamento import Departamento
from core.modulos.empresa.empresa import Empresa
from core.util.labels_property import LabesProperty
from core.util.util_manager import adiciona_form_control


class ClienteForm(forms.ModelForm):
    empresa = forms.ModelChoiceField(label="Empresa", queryset=None, widget=forms.Select())

    class Meta:
        model = Cliente
        fields = '__all__'
        exclude = ('senha', 'user')

    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)

        empresas = Empresa.objects.all()
        self.fields['empresa'].queryset = empresas
        print(dir(self.fields['departamento']))
        self.fields['departamento'].empty_label = '---------'
        # Select masters são as strings de retorno do ajax
        select_master_empresa = 'empresa'

        # Request Requisição Ajax Empresa
        self.fields['empresa'].widget.attrs['id'] = 'id_empresa'
        self.fields['empresa'].widget.attrs[
            'onchange'] = 'carregarElementoPorIdFK("' + reverse_lazy(
            "core:modulo:departamento:getDepartamentosPorIdEmpresa",
            kwargs={'idEmpresa': '00'}).__str__() + f'","id_empresa","id_departamento","{select_master_empresa}")'

        self.fields['departamento'].queryset = Departamento.objects.none()
        self.fields['perfil'].initial = 4 # Cliente id 3

        # Se o campo empresa possui algum dado atualizar o queryset
        if select_master_empresa in self.data:
            try:
                empresa_id = int(self.data.get('empresa'))
                self.fields['departamento'].queryset = Departamento.objects.filter(empresa_id=empresa_id).order_by(
                    'nome')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        # Se estiver editando o profissional recuperar dados já cadastrados inicialmente
        elif self.instance.pk:
            inicio = Cliente.objects.get(pk=self.instance.pk)
            dep = Departamento.objects.get(pk=inicio.departamento.pk)
            self.fields['departamento'].queryset = Departamento.objects.filter(empresa=dep.empresa).order_by(
                'nome')
            self.fields['empresa'].initial = dep.empresa
            self.fields['departamento'].initial = dep

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
        usuario = Cliente.objects.filter(usuario=login)
        user = User.objects.filter(username=login)
        if usuario.exists() or user.exists():
            self.add_error('usuario', LabesProperty.ERROR_NOME_USUARIO_EXISTE)

    def validarEmailUsuario(self, email):
        email = Cliente.objects.filter(email=email)
        if email.exists():
            self.add_error('email', LabesProperty.ERROR_EMAIL_USUARIO_EXISTE)
