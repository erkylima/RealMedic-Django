from django import forms
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from core.models import Paciente
from core.models.base.endereco import Endereco
from core.modulos.departamento.departamento import Departamento
from core.modulos.empresa.empresa import Empresa
from core.modulos.user_profile.user_profile import UserProfile
from core.util.util_manager import adiciona_form_control, get_user_type


class PacienteForm(forms.ModelForm):
    rua = forms.CharField(max_length=255, required=False)
    bairro = forms.CharField(max_length=100, required=False)
    cidade = forms.CharField(max_length=100, required=False)
    ESTADOS_CHOICES = (
        ('','---------'),
        ("AC", "Acre"),
        ("AL", "Alagoas"),
        ("AP", "Amapá"),
        ("AM", "Amazonas"),
        ("BA", "Bahia"),
        ("CE", "Ceará"),
        ("DF", "Distrito Federal"),
        ("ES", "Espírito Santo"),
        ("GO", "Goiás"),
        ("MA", "Maranhão"),
        ("MT", "Mato Grosso"),
        ("MS", "Mato Grosso do Sul"),
        ("MG", "Minas Gerais"),
        ("PA", "Pará"),
        ("PB", "Paraíba"),
        ("PR", "Paraná"),
        ("PE", "Pernambuco"),
        ("PI", "Piauí"),
        ("RJ", "Rio de Janeiro"),
        ("RN", "Rio Grande do Norte"),
        ("RS", "Rio Grande do Sul"),
        ("RO", "Rondônia"),
        ("RR", "Roraima"),
        ("SC", "Santa Catarina"),
        ("SP", "São Paulo"),
        ("SE", "Sergipe"),
        ("TO", "Tocantins"),

    )
    estado = forms.TypedChoiceField(choices=ESTADOS_CHOICES, required=False,empty_value='---------')
    numero = forms.IntegerField(required=False)
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
        self.fields['departamento'].required = True

        self.fields['departamento'].queryset = Departamento.objects.none()

        self.fields['data_nascimento'].initial = '01/01/2002'
        self.fields['cpf'].initial = ''
        self.fields['rg'].initial = ''
        self.fields['endereco'].initial= 0
        if isinstance(usuario, UserProfile):
            self.fields['departamento'].queryset = Departamento.objects.filter(
                empresa_id=usuario.userProfile.departamento.empresa_id)
        else:
            self.fields['departamento'].queryset = Departamento.objects.filter(
                empresa_id=usuario.userProfile.departamento.empresa_id)



        if self.instance.pk:
            inicio = Paciente.objects.get(pk=self.instance.pk)
            endereco = Endereco.objects.get(pk=self.instance.endereco_id)
            dep = Departamento.objects.get(pk=inicio.departamento.pk)
            self.fields['departamento'].queryset = Departamento.objects.filter(empresa=dep.empresa).order_by(
                'nome')
            self.fields['departamento'].initial = dep
            self.fields['departamento'].required = True
            self.fields['data_nascimento'].initial = self.instance.data_nascimento
            self.fields['cpf'].initial = self.instance.cpf
            self.fields['rg'].initial = self.instance.rg
            self.fields['rua'].initial =endereco.rua
            self.fields['cidade'].initial =endereco.cidade
            self.fields['estado'].initial =endereco.estado
            self.fields['numero'].initial =endereco.numero
        adiciona_form_control(self)


