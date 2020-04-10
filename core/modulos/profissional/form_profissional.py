from django import forms
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from core.models import Profissional, Empresa, DepartamentoProfissional, Departamento
from core.util.labels_property import LabesProperty
from core.util.util_manager import adiciona_form_control



class ProfissionalForm(forms.ModelForm):
    empresa = forms.ModelChoiceField(label="Empresa", queryset=None, widget=forms.Select())
    departamento = forms.ModelChoiceField(label="Departamento", queryset=Departamento.objects.none(), widget=forms.Select())

    class Meta:
        model = Profissional
        fields = '__all__'
        exclude = ('senha', 'user')

    def __init__(self, *args, **kwargs):
        super(ProfissionalForm, self).__init__(*args, **kwargs)
        instancia = self.instance
        empresas = Empresa.objects.all()
        self.fields['empresa'].queryset = empresas
        self.fields['departamento'].queryset = Departamento.objects.all()

        if instancia.pk:
            inicio = DepartamentoProfissional.objects.get(profissional=instancia.pk).departamento
            dep = Departamento.objects.get(pk=inicio.id)

            self.fields['empresa'].initial = dep.empresa
            self.fields['departamento'].initial = dep

        self.fields['empresa'].widget.attrs['id'] = 'id_empresa'
        self.fields['empresa'].widget.attrs[
            'onchange'] = 'carregarElementoPorIdFK("' + reverse_lazy("core:modulo:departamento:getDepartamentosPorIdEmpresa",
                                                                     kwargs={'idEmpresa': '00'}).__str__() + '","id_empresa","id_departamento")'

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
