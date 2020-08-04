from django import forms

from core.models import Prontuario
from core.util.util_manager import adiciona_form_control


class ProntuarioForm(forms.ModelForm):

    class Meta:
        model = Prontuario
        fields = '__all__'
        exclude = ('senha', 'user')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(ProntuarioForm, self).__init__(*args, **kwargs)

        adiciona_form_control(self)


