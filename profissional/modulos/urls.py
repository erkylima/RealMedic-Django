from django.urls import path, include

app_name = 'modulo'
urlpatterns = [
    path('meus_atendimentos/', include('profissional.modulos.meus_atendimentos.urls_meus_atendimentos'))
]