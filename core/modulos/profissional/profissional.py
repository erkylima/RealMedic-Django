from django.db import models

from core.models.base.time_stampable import Timestampable
from core.modulos.atendimentos_departamento.atendimentos_departamento import AtendimentosDepartamento
from core.modulos.departamento.departamento import Departamento
from core.modulos.tipo_profissional.tipo_profissional import TipoProfissional
from core.modulos.user_profile.user_profile import UserComum

class Profissional(Timestampable):
    class Meta:
        verbose_name = 'PROFISSIONAL'
        verbose_name_plural = 'PROFISSIONAIS'

    userComum = models.OneToOneField(UserComum, on_delete=models.PROTECT, related_name='profissional')
    codigo = models.CharField('Código', max_length=10,default="")
    descricao = models.CharField('Descrição', max_length=255, default="Um médico comum")
    tiposAtendimentos = models.ManyToManyField(AtendimentosDepartamento, verbose_name='Tipos de Atendimento')


    def __str__(self):
        return self.userComum.nome

    def getJson(self):
        return dict(
            id=self.pk,
            nome=self.userComum.nome,
            login=self.userComum.usuario,
            tipo='profissional',
            token=self.userComum.getToken(),
        )

    @property
    def getDepartamento(self):
        departamento = DepartamentoProfissional.objects.filter(profissional_id=self.pk)
        texto = departamento.first().departamento.empresa.nome_razao_social + " - "
        for dep in departamento:
            texto = texto + dep.departamento.nome + " "
        return texto

    @property
    def getNome(self):
        return self.userComum.nome

    def getUsuario(self):
        return self.userComum.usuario

    @property
    def getListAtributes(self):
        atributos = ['getNome', 'getUsuario', 'getDepartamento']
        inter_lista = []
        for row in atributos:
            field_value = getattr(self, row, None)
            inter_lista.append(field_value)
        return inter_lista

class DepartamentoProfissional(models.Model):
    class Meta:
        verbose_name = 'PROFISSIONAL DO DEPARTAMENTO'
        verbose_name_plural = 'PROFISSIONAIS DO DEPARTAMENTO'

    profissional = models.ForeignKey(Profissional, on_delete=models.PROTECT)
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT)
    tipo_profissional = models.ForeignKey(TipoProfissional, on_delete=models.PROTECT, default=1)

    def __str__(self):
        return self.profissional.userComum.nome + ' do ' + self.departamento.getNome()
