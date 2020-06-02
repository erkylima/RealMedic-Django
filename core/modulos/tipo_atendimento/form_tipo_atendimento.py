from django import forms
from datetime import datetime

from core.models import TipoAtendimento
from core.util.util_manager import adiciona_form_control


class TipoAtendimentoForm(forms.ModelForm):
    class Meta:
        model = TipoAtendimento
        fields = '__all__'
        # exclude = ('latLng',)

    def __init__(self, *args, **kwargs):
        super(TipoAtendimentoForm, self).__init__(*args, **kwargs)
        CHOICES = ([('00:30:00', '00h'), ('01:00:00', '01h'),
                   ('01:30:00', '01h'), ('02:00:00', '02h'),])
        self.fields['tempo_padrao'] = forms.ChoiceField(choices=CHOICES,label='Tempo Padrão', widget=forms.RadioSelect)
        if self.instance.pk:
            print(self.instance.tempo_padrao.strftime('%H:%M'))
            self.fields['tempo_padrao'].default = self.instance.tempo_padrao
        adiciona_form_control(self)
    #
    # def clean(self):
    #     cleaned_data = super(EmpresaForm, self).clean()
    #     # capacidade_do_tanque = cleaned_data.get('capacidade_do_tanque')
    #     # if capacidade_do_tanque == 0:
    #     #     self.add_error('capacidade_do_tanque', u'Capacidade do tanque inválida')
    #     self.add_error('nome_razao_social', u'Capacidade do tanque inválida')
