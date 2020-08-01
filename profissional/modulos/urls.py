from django.urls import path, include

app_name = 'modulo'
urlpatterns = [
    path('relatorio/', include('profissional.modulos.relatorio.urls_relatorio')),
    path('meus_atendimentos/', include('profissional.modulos.meus_atendimentos.urls_meus_atendimentos')),
    path('minha_escala/', include('profissional.modulos.minha_escala.urls_minha_escala')),
    path('meus_pacientes/', include('profissional.modulos.meus_pacientes.urls_meus_pacientes')),
]