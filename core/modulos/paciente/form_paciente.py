from django import forms
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from core.models import Paciente
from core.modulos.departamento.departamento import Departamento
from core.modulos.empresa.empresa import Empresa
from core.util.util_manager import adiciona_form_control


class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente
        fields = '__all__'
        exclude = ('senha', 'user')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(PacienteForm, self).__init__(*args, **kwargs)

        empresas = Empresa.objects.all()
        self.fields['departamento'].empty_label = '---------'
        self.fields['departamento'].required = False

        self.fields['departamento'].queryset = Departamento.objects.none()

        try:
            if self.user.userProfile: #verificar se é gerente
                self.fields['departamento'].queryset = Departamento.objects.filter(empresa_id=self.user.userProfile.empresa_id)
        except:
            if self.user.userAtendente:  # verificar se é gerente
                self.fields['departamento'].queryset = Departamento.objects.filter(
                    empresa_id=self.user.userAtendente.departamento.empresa_id)

        if self.instance.pk:
            inicio = Paciente.objects.get(pk=self.instance.pk)
            dep = Departamento.objects.get(pk=inicio.departamento.pk)
            self.fields['departamento'].queryset = Departamento.objects.filter(empresa=dep.empresa).order_by(
                'nome')
            self.fields['departamento'].initial = dep

        adiciona_form_control(self)


