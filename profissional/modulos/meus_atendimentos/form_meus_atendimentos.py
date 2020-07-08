from django import forms

from core.models import Atendimento
from core.util.util_manager import adiciona_form_control


class MeusAtendimentosForm(forms.ModelForm):
    class Meta:
        model = Atendimento
        fields = '__all__'
        # exclude = ('latLng',)

    def __init__(self, *args, **kwargs):
        super(MeusAtendimentosForm, self).__init__(*args, **kwargs)
        adiciona_form_control(self)
