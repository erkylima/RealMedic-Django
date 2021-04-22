import subprocess
import traceback

from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.decorators import login_required, permission_required
from django.http import JsonResponse
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from core.modulos.atendente.atendente import Atendente
from core.modulos.gerente.gerente import Gerente
from core.modulos.profissional.profissional import Profissional
from core.modulos.user_profile.user_profile import UserProfile
from core.util.util_manager import get_user_type


@login_required()
def index(request):
    print('INDEX')
    return LoginView.redirect_after_login(self=LoginView, user=request.user)


class LoginView(TemplateView):
    template_name = 'core/login.html'
    def get(self, request, *args, **kwargs):
        print('GET')
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print("POST")
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            django_login(request, user)
            return self.redirect_after_login(user)

        message = 'Usuário ou senha incorretos!!'
        return self.render_to_response({'message': message})

    def redirect_after_login(self, user):
        print('redirect_after_login')
        usuario = get_user_type(user)

        if user.is_superuser:
            return redirect('/admin/')
        elif isinstance(usuario, Gerente):
            return redirect('/core/')
        elif isinstance(usuario, Profissional):
            return redirect('/profissional/app/relatorio/')
        elif isinstance(usuario, Atendente):
            return redirect('/core/')
        else:
            message = 'Usuário sem permissão!!'
            return self.render_to_response({'message': message})

from django.conf import settings



@login_required()
def deploy(request):
    print('backup')
    try:
        if request.user.is_superuser:
            print('INICIO')
            # subprocess.call([
            #     "ls"])

            # condição
            # folder = 'covid_19'

            # dev = 'dev.' in request.build_absolute_uri()
            debug = settings.DEBUG

            # if debug is True:
            #     folder = 'covid_19_dev'
            #     gunicorn_name = 'covid_19_dev'
            #
            # else:
            folder = 'realconsulta'
            nome_projeto = 'RealMedic-Django'
            gunicorn_name = 'realconsulta'

            projeto = '/webapps/{}/{}/'.format(folder, nome_projeto)

            print('PASSO 1_________________________')
            subprocess.call([
                "sudo",
                "git",
                "pull"], cwd=projeto)

            pip = '/webapps/{}/bin/pip'.format(folder)
            python = '/webapps/{}/bin/python'.format(folder)
            manage = '/webapps/{}/{}/manage.py'.format(folder, nome_projeto)

            print('PASSO 2_________________________')
            subprocess.call([pip,
                             "install",
                             "-r",
                             "requerimentos.txt",
                             ], cwd=projeto)

            print('PASSO 3_________________________')
            subprocess.call([python,
                             manage,
                             "migrate"])
            print('PASSO 4_________________________')
            subprocess.call([python,
                             manage,
                             "collectstatic", "--noinput"])
            print('PASSO 5_________________________')
            subprocess.call(["sudo",
                             "supervisorctl",
                             "restart",
                             gunicorn_name])

            return JsonResponse({'ok': True})

    except Exception as e:
        traceback.print_exc()
        print(e)
        return JsonResponse({'ok': False})