from django.urls import path, include

from core import views_core

app_name = 'core'
urlpatterns = [
    path('', views_core.index),
    path('login/', views_core.LoginView.as_view(), name='login'),
    path('pages/', include('core.modulos.urls')),
]
