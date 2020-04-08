from django import forms

from core.models import Departamento
from core.util.util_manager import adiciona_form_control


class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = '__all__'
        # exclude = ('latLng',)

    def __init__(self, *args, **kwargs):
        super(DepartamentoForm, self).__init__(*args, **kwargs)
        adiciona_form_control(self)
    #
    # def clean(self):
    #     cleaned_data = super(DepartamentoForm, self).clean()
    #     # capacidade_do_tanque = cleaned_data.get('capacidade_do_tanque')
    #     # if capacidade_do_tanque == 0:
    #     #     self.add_error('capacidade_do_tanque', u'Capacidade do tanque inválida')
    #     self.add_error('nome_razao_social', u'Capacidade do tanque inválida')
