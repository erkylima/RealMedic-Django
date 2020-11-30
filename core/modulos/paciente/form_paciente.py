from django import forms
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from core.models import Paciente
from core.modulos.departamento.departamento import Departamento
from core.modulos.empresa.empresa import Empresa
from core.modulos.user_profile.user_profile import UserProfile
from core.util.util_manager import adiciona_form_control, get_user_type


class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente
        fields = '__all__'
        exclude = ('senha', 'user')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(PacienteForm, self).__init__(*args, **kwargs)
        usuario = get_user_type(self.user)

        empresas = Empresa.objects.all()
        self.fields['departamento'].empty_label = '---------'
        self.fields['departamento'].required = False

        self.fields['departamento'].queryset = Departamento.objects.none()
        if isinstance(usuario, UserProfile):
            self.fields['departamento'].queryset = Departamento.objects.filter(
                empresa_id=usuario.empresa_id)
        else:
            self.fields['departamento'].queryset = Departamento.objects.filter(
                empresa_id=usuario.departamento.empresa_id)



        if self.instance.pk:
            inicio = Paciente.objects.get(pk=self.instance.pk)
            dep = Departamento.objects.get(pk=inicio.departamento.pk)
            self.fields['departamento'].queryset = Departamento.objects.filter(empresa=dep.empresa).order_by(
                'nome')
            self.fields['departamento'].initial = dep

        adiciona_form_control(self)


