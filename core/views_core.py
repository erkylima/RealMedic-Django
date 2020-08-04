from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView


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
        if user.is_superuser:
            return redirect('/admin/')
        else:
            try:
                if user.userProfile:
                    return redirect('/core/')
            except:
                try:
                    if user.userAtendente:
                        return redirect('/core/')
                except:
                    return redirect('/profissional/app/relatorio/relatorio/')
        # message = 'Usuário sem permissão!!'
        # return self.render_to_response({'message': message})
