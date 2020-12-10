from django.urls import path, include

from core import views_core

app_name = 'core'
urlpatterns = [
    path('', views_core.index),
    path('login/', views_core.LoginView.as_view(), name='login'),
    path('core/', include('core.modulos.urls')),

    path('deploy/', views_core.deploy, name='deploy'),
]
