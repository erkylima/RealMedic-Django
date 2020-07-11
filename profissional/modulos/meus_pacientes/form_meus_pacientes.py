from django import forms

from core.models import Paciente
from core.util.util_manager import adiciona_form_control


class MeusPacientesForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
        # exclude = ('latLng',)

    def __init__(self, *args, **kwargs):
        super(MeusPacientesForm, self).__init__(*args, **kwargs)
        adiciona_form_control(self)
