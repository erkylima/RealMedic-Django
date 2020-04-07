from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from core.util.util_manager import MyLabls


class DashBoard(MyLabls, LoginRequiredMixin, TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        print('get_context_data')
        context = super().get_context_data(**kwargs)
        dados = {}
        context.update(dados)
        print('context', context)
        return context
