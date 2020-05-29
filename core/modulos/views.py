from django.contrib import auth
from django.contrib.auth import user_logged_out
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.core import serializers

from core.models import Atendimento
from core.util.util_manager import MyLabls


class DashBoard(MyLabls, LoginRequiredMixin, TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        print('get_context_data')
        context = super().get_context_data(**kwargs)
        atendimentos = Atendimento.objects.all()
        dados = {}
        test = list(Atendimento.objects.values())

        context['atendimentos'] = test
        print(context['atendimentos'])
        context.update(dados)

        return context

@login_required
def logout_view(request):
    user = getattr(request, 'user', None)
    user = None
    user_logged_out.send(sender=user.__class__, request=request, user=user)


    from django.contrib.auth.models import AnonymousUser
    request.user = AnonymousUser()
    # Redirect to a success page.
    return HttpResponseRedirect(reverse('core:login'))