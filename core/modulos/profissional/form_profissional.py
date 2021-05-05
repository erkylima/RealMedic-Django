from django import forms
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from core.models import DepartamentoProfissional, Departamento,TipoProfissional
from core.modulos.atendimentos_departamento.atendimentos_departamento import AtendimentosDepartamento
from core.modulos.profissional.profissional import Profissional

from core.util.labels_property import LabesProperty
from core.util.util_manager import adiciona_form_control, get_user_type


class ProfissionalForm(forms.ModelForm):
    # empresa = forms.ModelChoiceField(label="Empresa", queryset=None, widget=forms.Select())
    departamento = forms.ModelChoiceField(label="Departamento", queryset=Departamento.objects.none(), widget=forms.Select())
    tipo_profissional = forms.ModelChoiceField(label="Especialidade", queryset=TipoProfissional.objects.all(), widget=forms.Select())
    # codigo = forms.CharField(label="Código")
    nome = forms.CharField(label="Nome")
    descricao = forms.CharField(label="Descrição")
    usuario = forms.CharField(label="Usuário")
    email = forms.CharField(label="Email")

    class Meta:
        model = Profissional
        fields = '__all__'
        exclude = ('senha', 'user')


    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')

        super(ProfissionalForm, self).__init__(*args, **kwargs)
        usuario = get_user_type(self.user)
        instancia = self.instance
        departamentos = Departamento.objects.filter(empresa_id=usuario.userProfile.departamento.empresa_id)
        # Select masters são as strings de retorno do ajax
        # select_master_empresa = 'empresa'
        select_master_departamento = 'departamento'
        self.fields['departamento'].queryset = departamentos
        # self.fields['perfil'].required = False
        self.fields['userComum'].required = False

        # # Request Requisição Ajax Empresa
        # self.fields['empresa'].widget.attrs['id'] = 'id_empresa'
        # self.fields['empresa'].widget.attrs[
        #     'onchange'] = 'carregarElementoPorIdFK("' + reverse_lazy(
        #     "core:modulo:departamento:getDepartamentosPorIdEmpresa",
        #     kwargs={'idEmpresa': '00'}).__str__() + f'","id_empresa","id_departamento","{select_master_empresa}")'

        # Request Requisição Ajax Departamento
        # self.fields['departamento'].widget.attrs[
        #     'onchange'] = 'carregarElementoPorIdFK("' + reverse_lazy(
        #     "core:modulo:tipo_atendimento:getTiposAtendimentosPorIdTipoProfissional",
        #     kwargs={
        #         'idTipoProfissional': '00'}).__str__() + f'","id_departamento","id_tiposAtendimentos","{select_master_departamento}")'

        # Request Requisição Ajax Tipo Profissional
        print('link'+reverse_lazy(
            "core:modulo:tipo_atendimento:getTiposAtendimentosPorIdTipoProfissional",
            kwargs={
                'idTipoProfissional': '00','idDepartamento':'00'}).__str__()+ f'","id_tipo_profissional","id_tiposAtendimentos","{select_master_departamento}")')
        self.fields['tipo_profissional'].widget.attrs[
            'onchange'] = 'carregarElementoPorIdFK("' + reverse_lazy(
            "core:modulo:tipo_atendimento:getTiposAtendimentosPorIdTipoProfissional",
            kwargs={
                'idTipoProfissional': '00','idDepartamento':'11'}).__str__() + f'","id_tipo_profissional","id_tiposAtendimentos","{select_master_departamento}")'        # Se o campo empresa possui algum dado atualizar o queryset
        # self.fields['perfil'].initial = Group.objects.get(name='Profissional').pk # Pegar id do grupo de permissão Profissional

        if select_master_departamento in self.data:
            try:
                departamento_id = int(self.data.get('departamento'))

                self.fields['tiposAtendimentos'].queryset = AtendimentosDepartamento.objects.filter(
                    departamento_id=departamento_id).order_by(
                    'tipo_atendimento__descricao')
                print(self.fields['tiposAtendimentos'].queryset)
            except (ValueError, TypeError):
                pass
        # Se estiver editando o profissional recuperar dados já cadastrados inicialmente
        elif self.instance.pk:
            inicio = DepartamentoProfissional.objects.get(profissional=instancia)
            dep = Departamento.objects.get(pk=inicio.departamento.pk)
            tipo = TipoProfissional.objects.get(pk=inicio.tipo_profissional_id)
            self.fields['departamento'].queryset = Departamento.objects.filter(empresa=dep.empresa).order_by(
                'nome')
            self.fields['departamento'].initial = dep
            self.fields['tiposAtendimentos'].queryset = AtendimentosDepartamento.objects.filter(
                departamento_id=dep.pk,tipo_profissional=tipo.pk).order_by(
                'tipo_atendimento__descricao')

            self.fields['tiposAtendimentos'].initial = inicio.profissional.tiposAtendimentos
            self.fields['tipo_profissional'].initial = tipo
            self.fields['nome'].initial = inicio.profissional.userComum.nome
            self.fields['email'].initial = inicio.profissional.userComum.email
            self.fields['usuario'].initial = inicio.profissional.userComum.usuario
            self.fields['codigo'].initial = inicio.profissional.codigo

        else:
            self.fields['tiposAtendimentos'].queryset = AtendimentosDepartamento.objects.none()        # Se o campo departamento possui algum dado atualizar o queryset
          # invalid input from the client; ignore and fallback to empty City queryset

        adiciona_form_control(self)

    def clean(self):
        instancia = self.instance
        print('clean')
        login = self.cleaned_data.get('usuario', None)
        email = self.cleaned_data.get('email', None)
        if instancia.codigo == "":
            self.validarLoginUsuario(login)
            self.validarEmailUsuario(email)
        else:
            if instancia.userComum.usuario != login:
                self.validarLoginUsuario(login)
            if instancia.userComum.email != email:
                self.validarEmailUsuario(email)

    def validarLoginUsuario(self, login):
        usuario = Profissional.objects.filter(userComum__usuario=login)
        user = User.objects.filter(username=login)
        if usuario.exists() or user.exists():
            self.add_error('usuario', LabesProperty.ERROR_NOME_USUARIO_EXISTE)

    def validarEmailUsuario(self, email):
        email = Profissional.objects.filter(userComum__email=email)
        if email.exists():
            self.add_error('email', LabesProperty.ERROR_EMAIL_USUARIO_EXISTE)
