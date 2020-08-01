from django import forms
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from core.models import Paciente
from core.modulos.departamento.departamento import Departamento
from core.modulos.empresa.empresa import Empresa
from core.util.util_manager import adiciona_form_control


class PacienteForm(forms.ModelForm):
    empresa = forms.ModelChoiceField(label="Empresa", queryset=None, widget=forms.Select(), required=False)

    class Meta:
        model = Paciente
        fields = '__all__'
        exclude = ('senha', 'user')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(PacienteForm, self).__init__(*args, **kwargs)

        empresas = Empresa.objects.all()
        self.fields['empresa'].queryset = empresas
        self.fields['departamento'].empty_label = '---------'
        self.fields['departamento'].required = False

        # Select masters são as strings de retorno do ajax
        select_master_empresa = 'empresa'

        # Request Requisição Ajax Empresa
        self.fields['empresa'].widget.attrs['id'] = 'id_empresa'
        self.fields['empresa'].widget.attrs[
            'onchange'] = 'carregarElementoPorIdFK("' + reverse_lazy(
            "core:modulo:departamento:getDepartamentosPorIdEmpresa",
            kwargs={'idEmpresa': '00'}).__str__() + f'","id_empresa","id_departamento","{select_master_empresa}")'

        self.fields['departamento'].queryset = Departamento.objects.none()

        if self.user.userProfile: #verificar se é gerente
            self.fields['departamento'].queryset = Departamento.objects.filter(empresa=self.user.userProfile.empresa_id)

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
            inicio = Paciente.objects.get(pk=self.instance.pk)
            dep = Departamento.objects.get(pk=inicio.departamento.pk)
            self.fields['departamento'].queryset = Departamento.objects.filter(empresa=dep.empresa).order_by(
                'nome')
            self.fields['empresa'].initial = dep.empresa
            self.fields['departamento'].initial = dep

        adiciona_form_control(self)


