from django import forms
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from core.models import Profissional, Empresa, DepartamentoProfissional, Departamento,TipoProfissional
from core.util.labels_property import LabesProperty
from core.util.util_manager import adiciona_form_control



class ProfissionalForm(forms.ModelForm):
    empresa = forms.ModelChoiceField(label="Empresa", queryset=None, widget=forms.Select())
    departamento = forms.ModelChoiceField(label="Departamento", queryset=Departamento.objects.none(), widget=forms.Select())
    tipo_profissional = forms.ModelChoiceField(label="Tipo de Profissional", queryset=Empresa.objects.none(), widget=forms.Select())

    class Meta:
        model = Profissional
        fields = '__all__'
        exclude = ('senha', 'user')

    def __init__(self, *args, **kwargs):
        super(ProfissionalForm, self).__init__(*args, **kwargs)
        instancia = self.instance
        empresas = Empresa.objects.all()
        self.fields['empresa'].queryset = empresas

        # Select masters são as strings de retorno do ajax
        select_master_empresa = 'empresa'
        select_master_departamento = 'departamento'

        # Request Requisição Ajax Empresa
        self.fields['empresa'].widget.attrs['id'] = 'id_empresa'
        self.fields['empresa'].widget.attrs[
            'onchange'] = 'carregarElementoPorIdFK("' + reverse_lazy(
            "core:modulo:departamento:getDepartamentosPorIdEmpresa",
            kwargs={'idEmpresa': '00'}).__str__() + f'","id_empresa","id_departamento","{select_master_empresa}")'

        # Request Requisição Ajax Departamento
        self.fields['departamento'].widget.attrs[
            'onchange'] = 'carregarElementoPorIdFK("' + reverse_lazy(
            "core:modulo:tipo_profissional:getTipoProfissionalPorIdDepartamento",
            kwargs={'idDepartamento': '00'}).__str__() + f'","id_departamento","id_tipo_profissional","{select_master_departamento}")'

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
            inicio = DepartamentoProfissional.objects.get(profissional=instancia)
            dep = Departamento.objects.get(pk=inicio.departamento.pk)
            tipo = TipoProfissional.objects.get(pk=inicio.tipo_profissional_id)
            self.fields['departamento'].queryset = Departamento.objects.filter(empresa=dep.empresa).order_by(
                'nome')
            self.fields['tipo_profissional'].queryset = inicio.tipo_profissional.departamento.tipoprofissional_set
            self.fields['empresa'].initial = dep.empresa
            self.fields['departamento'].initial = dep
            self.fields['tipo_profissional'].initial = tipo

        # Se o campo departamento possui algum dado atualizar o queryset
        if select_master_departamento in self.data:
            try:
                departamento_id = int(self.data.get('departamento'))
                self.fields['tipo_profissional'].queryset = TipoProfissional.objects.filter(departamento_id=departamento_id).order_by(
                    'descricao')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset

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
        usuario = Profissional.objects.filter(usuario=login)
        user = User.objects.filter(username=login)
        if usuario.exists() or user.exists():
            self.add_error('usuario', LabesProperty.ERROR_NOME_USUARIO_EXISTE)

    def validarEmailUsuario(self, email):
        email = Profissional.objects.filter(email=email)
        if email.exists():
            self.add_error('email', LabesProperty.ERROR_EMAIL_USUARIO_EXISTE)
