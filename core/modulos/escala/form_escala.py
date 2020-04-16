from django import forms

from core.models import Escala
from core.util.util_manager import adiciona_form_control


class EscalaForm(forms.ModelForm):
    class Meta:
        model = Escala
        fields = '__all__'
        # exclude = ('latLng',)

    def __init__(self, *args, **kwargs):
        super(EscalaForm, self).__init__(*args, **kwargs)
        self.fields['dia'].input_formats  = ['%Y-%m-%d',
                                             '%m/%d/%Y',
                                             '%m/%d/%y',
                                             '%b %d %Y',
                                             '%b %d, %Y',
                                             '%d %b %Y',
                                             '%d %b, %Y',
                                             '%B %d %Y',
                                             '%B %d, %Y',
                                             '%d %B %Y',
                                             '%d %B, %Y']


        adiciona_form_control(self)
    #
    # def clean(self):
    #     cleaned_data = super(EmpresaForm, self).clean()
    #     # capacidade_do_tanque = cleaned_data.get('capacidade_do_tanque')
    #     # if capacidade_do_tanque == 0:
    #     #     self.add_error('capacidade_do_tanque', u'Capacidade do tanque inválida')
    #     self.add_error('nome_razao_social', u'Capacidade do tanque inválida')
