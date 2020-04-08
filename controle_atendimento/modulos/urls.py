from django.urls import path, include

from core.modulos import views

app_name = 'modulo'
urlpatterns = [
    # path('', views.DashBoard.as_view(), name='dashboard'),
    path('empresa/', include('core.modulos.empresa.urls_empresa')),
]
