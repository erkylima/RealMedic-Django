from django.urls import path, include


app_name = 'profissional'
urlpatterns = [
    path('app/', include('profissional.modulos.urls'))
]
