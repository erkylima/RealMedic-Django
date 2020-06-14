from django.urls import path, include

app_name = 'modulo'
urlpatterns = [
    path('marcar/', include('cliente.modulos.marca_atendimento.urls_atendimento'))
]