from django import forms
from django.urls import reverse_lazy

from core.modulos.atendimentos_departamento.atendimentos_departamento import AtendimentosDepartamento
from core.modulos.departamento.departamento import Departamento
from core.modulos.user_profile.user_profile import UserProfile
from core.util.util_manager import adiciona_form_control, get_user_type


class AtendimentosDepartamentoForm(forms.ModelForm):
    class Meta:
        model = AtendimentosDepartamento
        fields = '__all__'
        # exclude = ('latLng',)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(AtendimentosDepartamentoForm, self).__init__(*args, **kwargs)
        select_master_tipo_profissional = 'tipo_profissional'
        usuario = get_user_type(self.user)

        print("OLa" + reverse_lazy(
            "core:modulo:atendimentos_departamento:getTiposAtendimentosPorIdTipoProfissional",
            kwargs={
                'idTipoAtendimento': '00'}).__str__() + f'","id_tipo_atendimento","id_tipo_profissional","{select_master_tipo_profissional}")')
        self.fields['tipo_atendimento'].widget.attrs[
            'onchange'] = 'carregarIdTipoProfissionalPorIdFK("' + reverse_lazy(
            "core:modulo:atendimentos_departamento:getTiposAtendimentosPorIdTipoProfissional",
            kwargs={
                'idTipoAtendimento': '00'}).__str__() + f'","id_tipo_atendimento","id_tipo_profissional","{select_master_tipo_profissional}")'
        self.fields['tipo_atendimento'].empty_label = '---------'
        self.fields['tipo_atendimento'].initial = 0


        self.fields['departamento'].queryset = Departamento.objects.filter(empresa_id=usuario.userProfile.departamento.empresa_id)

        CHOICES = ([('00:10:00', '00h'), ('00:20:00', '00h'), ('00:30:00', '00h'), ('00:40:00', '00h'),('00:50:00', '00h'),
                    ('01:00:00', '01h'), ('01:10:00', '01h'), ('01:20:00', '01h'), ('01:30:00', '01h'), ('01:40:00', '01h'), ('01:50:00', '01h'), ('02:00:00', '02h'),])
        self.fields['tempo_padrao'] = forms.ChoiceField(choices=CHOICES,label='Tempo Padrão', widget=forms.RadioSelect)
        if select_master_tipo_profissional in self.data:
            print("teste")

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
