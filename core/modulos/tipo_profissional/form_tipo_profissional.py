from django import forms
from django.urls import reverse_lazy

from core.models import TipoProfissional, Empresa, Departamento
from core.util.util_manager import adiciona_form_control


class TipoProfissionalForm(forms.ModelForm):
    empresa = forms.ModelChoiceField(label="Empresa", queryset=Empresa.objects.all(), widget=forms.Select())

    class Meta:
        model = TipoProfissional
        fields = '__all__'
        # exclude = ('latLng',)

    def __init__(self, *args, **kwargs):
        super(TipoProfissionalForm, self).__init__(*args, **kwargs)

        select_master_empresa = 'empresa'
        print(self.fields)
        self.fields['empresa'].widget.attrs['id'] = 'id_empresa'
        self.fields['empresa'].widget.attrs[
            'onchange'] = 'carregarElementoPorIdFK("' + reverse_lazy(
            "core:modulo:departamento:getDepartamentosPorIdEmpresa",
            kwargs={'idEmpresa': '00'}).__str__() + f'","id_empresa","id_departamento","{select_master_empresa}")'

        self.fields['departamento'].queryset = Departamento.objects.none()

        if select_master_empresa in self.data:
            try:
                empresa_id = int(self.data.get('empresa'))
                self.fields['departamento'].queryset = Departamento.objects.filter(empresa_id=empresa_id).order_by(
                    'nome')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['departamento'].queryset = Departamento.objects.filter(empresa_id = self.instance.departamento.empresa_id)
            self.fields['departamento'].initial = self.instance.departamento
            self.fields['empresa'].initial = self.instance.departamento.empresa

        adiciona_form_control(self)
    #
    # def clean(self):
    #     cleaned_data = super(EmpresaForm, self).clean()
    #     # capacidade_do_tanque = cleaned_data.get('capacidade_do_tanque')
    #     # if capacidade_do_tanque == 0:
    #     #     self.add_error('capacidade_do_tanque', u'Capacidade do tanque inválida')
    #     self.add_error('nome_razao_social', u'Capacidade do tanque inválida')
