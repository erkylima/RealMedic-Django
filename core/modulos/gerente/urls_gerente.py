from django.urls import path

from core.modulos.user_profile import views_user_profile

app_name = 'gerente'
urlpatterns = [
    path('list', views_user_profile.UserProfileListView.as_view(), name='list_view'),
    path('create', views_user_profile.UserProfileCreateView.as_view(), name='create_view'),
    path('update/<int:pk>', views_user_profile.UserProfileUpdateView.as_view(), name='update_view'),
]
