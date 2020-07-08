from django.urls import path, include

from core.modulos import views

app_name = 'modulo'
urlpatterns = [
    path('', views.DashBoard.as_view(), name='dashboard'),
    path('empresa/', include('core.modulos.empresa.urls_empresa')),
    path('usuario/', include('core.modulos.user_profile.urls_user_profile')),
    path('departamento/', include('core.modulos.departamento.urls_departamento')),
    path('atendente/', include('core.modulos.atendente.urls_atendente')),
    path('cliente/', include('core.modulos.cliente.urls_cliente')),
    path('paciente/', include('core.modulos.paciente.urls_paciente')),
    path('profissional/', include('core.modulos.profissional.urls_profissional')),
    path('tipo_profissional/', include('core.modulos.tipo_profissional.urls_tipo_profissional')),
    path('tipo_atendimento/', include('core.modulos.tipo_atendimento.urls_tipo_atendimento')),
    path('escala/', include('core.modulos.escala.urls_escala')),
    path('atendimento/', include('core.modulos.atendimento.urls_atendimento')),
    path('logout/',views.logout_view, name="sair")

    # path('professionals/', include('core.modulos.professional.urls')),
    # path('health_tips/', include('core.modulos.health_tips.urls')),
    # path('daily_newsletter/', include('core.modulos.daily_newsletter.urls')),
    # path('blog_post/', include('core.modulos.blog_post.urls')),
    # path('health_center/', include('core.modulos.health_center.urls')),
]
