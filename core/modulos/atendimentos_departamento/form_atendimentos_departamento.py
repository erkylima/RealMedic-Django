from django import forms
from django.urls import reverse_lazy

from core.modulos.atendimentos_departamento.atendimentos_departamento import AtendimentosDepartamento
from core.modulos.departamento.departamento import Departamento
from core.modulos.tipo_atendimento.tipo_atendimento import TipoAtendimento
from core.modulos.tipo_profissional.tipo_profissional import TipoProfissional
from core.modulos.user_profile.user_profile import UserProfile
from core.util.util_manager import adiciona_form_control, get_user_type


class AtendimentosDepartamentoForm(forms.ModelForm):
    tipo_profissional = forms.ModelChoiceField(label="Especialidade",
                                               queryset=TipoProfissional.objects.all(), widget=forms.Select())
    class Meta:
        model = AtendimentosDepartamento
        fields = '__all__'
        # exclude = ('latLng',)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(AtendimentosDepartamentoForm, self).__init__(*args, **kwargs)
        select_master_tipo_profissional = 'tipo_profissional'
        usuario = get_user_type(self.user)
        select_master_departamento = 'departamento'

        self.fields['tipo_profissional'].widget.attrs[
            'onchange'] = 'carregarElementoPorIdFK("' + reverse_lazy(
            "core:modulo:atendimentos_departamento:getTiposAtendimentosPorIdTipoProfissional",
            kwargs={
                'idTipoAtendimento': '00'}).__str__() + f'","id_tipo_profissional","id_tipo_atendimento","{select_master_departamento}")'  # Se o campo empresa possui algum dado atualizar o queryset
        self.fields['departamento'].empty_label = '---------'
        self.fields['departamento'].initial = 0

        self.fields['tipo_atendimento'].empty_label = '---------'
        self.fields['tipo_atendimento'].queryset = TipoAtendimento.objects.none()
        self.fields['tipo_atendimento'].widget.attrs['readonly'] = True


        self.fields['departamento'].queryset = Departamento.objects.filter(empresa_id=usuario.userProfile.departamento.empresa_id)

        CHOICES = ([('00:10:00', '00h'), ('00:20:00', '00h'), ('00:30:00', '00h'), ('00:40:00', '00h'),('00:50:00', '00h'),
                    ('01:00:00', '01h'), ('01:10:00', '01h'), ('01:20:00', '01h'), ('01:30:00', '01h'), ('01:40:00', '01h'), ('01:50:00', '01h'), ('02:00:00', '02h'),])
        self.fields['tempo_padrao'] = forms.ChoiceField(choices=CHOICES,label='Tempo Padrão', widget=forms.RadioSelect)
        if select_master_tipo_profissional in self.data:
            print("teste")

        if select_master_departamento in self.data:
            try:
                id_tipo_profissional = int(self.data.get('tipo_profissional'))

                self.fields['tipo_atendimento'].queryset = TipoAtendimento.objects.filter(tipo_profissional_id=id_tipo_profissional)
                print(self.fields['tipo_atendimento'].queryset)
            except (ValueError, TypeError):

                pass

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
