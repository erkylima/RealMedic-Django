from django import forms

from core.models import DepartamentoProfissional
from core.util.util_manager import adiciona_form_control


class AtendimentoForm(forms.ModelForm):
    class Meta:
        model = DepartamentoProfissional
        fields = '__all__'
        # exclude = ('latLng',)

    def __init__(self, *args, **kwargs):
        super(AtendimentoForm, self).__init__(*args, **kwargs)
        adiciona_form_control(self)
    #
    # def clean(self):
    #     cleaned_data = super(AtendimentoForm, self).clean()
    #     # capacidade_do_tanque = cleaned_data.get('capacidade_do_tanque')
    #     # if capacidade_do_tanque == 0:
    #     #     self.add_error('capacidade_do_tanque', u'Capacidade do tanque inválida')
    #     self.add_error('nome_razao_social', u'Capacidade do tanque inválida')
