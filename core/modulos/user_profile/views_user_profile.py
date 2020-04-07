from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from core.models import UserProfile
from core.modulos.user_profile.form_user_profile import UserProfileForm
from core.util.labels_property import LabesProperty
from core.util.util_manager import MyListViewSearcheGeneric, MyLabls


class MyListViewUserProfile(LoginRequiredMixin,
                            MyListViewSearcheGeneric,
                            MyLabls,
                            ListView):
    allow_empty = True
    paginate_by = 10

    # permission_required = 'global_permissions.controla_licitacao'
    # permission_denied_message = 'Permission Denied'


class MyCreateViewUserProfile(LoginRequiredMixin, MyLabls, CreateView):
    # permission_required = 'global_permissions.controla_licitacao'
    # permission_denied_message = 'Permission Denied'
    pass


class MyUpdateViewUserProfile(LoginRequiredMixin, MyLabls, UpdateView):
    # permission_required = 'global_permissions.controla_licitacao'
    # permission_denied_message = 'Permission Denied'
    pass


class UserProfileListView(MyListViewUserProfile):
    template_name = 'user_profile/templates/list_view_user_profile.html'
    model = UserProfile
    search_fields = ['nome', 'usuario']
    COLUMNS = [LabesProperty.NOME, LabesProperty.USUARIO, LabesProperty.PERFIL]
    NAME_MODEL = UserProfile._meta.verbose_name
    NAME_MODEL_PLURAL = UserProfile._meta.verbose_name_plural
    PAGE_CREATE_VIEW = reverse_lazy('core:pages:usuario:create_view')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context


class UserProfileCreateView(MyCreateViewUserProfile):
    template_name = 'user_profile/templates/create_view_user_profile.html'
    model = UserProfile
    form_class = UserProfileForm
    success_url = reverse_lazy('core:pages:usuario:list_view')
    NAME_MODEL = UserProfile._meta.verbose_name

    def form_invalid(self, form):
        print(form.errors, len(form.errors))
        return super(UserProfileCreateView, self).form_invalid(form)

    def form_valid(self, form):

        userProfile = form.save(commit=False)
        # TODO - Veriricar a estratégia de senha
        user = User.objects.create_user(
            username=userProfile.usuario,
            password='admin123admin',
        )
        # user.groups.add(userProfile.group)
        # user.save()
        userProfile.user = user
        userProfile.save()
        self.request.session['save_model'] = 'true'
        return super().form_valid(form)


class UserProfileUpdateView(MyUpdateViewUserProfile):
    template_name = 'user_profile/templates/create_view_user_profile.html'
    model = UserProfile
    form_class = UserProfileForm
    success_url = reverse_lazy('core:pages:usuario:list_view')
    NAME_MODEL = UserProfile._meta.verbose_name

    def form_invalid(self, form):
        print(form.errors, len(form.errors))
        return super(UserProfileUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        self.request.session['update_model'] = 'true'
        return super().form_valid(form)
