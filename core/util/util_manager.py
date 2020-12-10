import datetime


from dateutil.relativedelta import relativedelta
from django import forms
from django.shortcuts import redirect
from extra_views import SearchableListMixin
from core.util.labels_property import LabesProperty
from django.db import models

def get_data_por_idade(idade): # Retorna a idade em datetime
    today = datetime.date.today()
    idade = (today - relativedelta(years=idade))
    return idade

def get_idade_por_data(data): # Retorna a conversão da data para idade
    today = datetime.date.today()
    idade = (today - relativedelta(years=data.year)).year
    return idade

class ValidarEmpresa:
    def dispatch(self, request, *args, **kwargs):
        usuario = get_user_type(request.user)
        if not request.user.is_authenticated:
            return redirect('core:login')
        try:
            if usuario.departamento.empresa ==  self.get_object().departamento.empresa:
                return super().dispatch(request, *args, **kwargs) 
            else:
                return redirect('core:modulo:dashboard')
        except:
            try:
                if usuario.empresa ==  self.get_object().departamento.empresa:
                    return super().dispatch(request, *args, **kwargs)
                else:
                    return redirect('core:modulo:dashboard')
            except:
                # departamento_profissional = DepartamentoProfissional.objects.get(profissional_id=request.user.userProfissional.pk)
                # print(self.get_object().departamentoProfissional.pk)
                # departamento_profissional_do_objeto = DepartamentoProfissional.objects.get(profissional_id=self.get_object().pk)
                
                # if departamento_profissional.de*partamento.empresa == departamento_profissional_do_objeto.departamento.empresa:
                return super().dispatch(request, *args, **kwargs)
                # else:
                #     return redirect('profissional:modulo:relatorio:ver')

def adiciona_form_control(self):
    for field_name, field in self.fields.items():

        if field and isinstance(field, forms.ModelChoiceField):
            field.widget.attrs['class'] = 'form-control select2'

            # field.widget.attrs['multiple'] = 'multiple'
        elif field and isinstance(field, forms.TypedChoiceField):
            field.widget.attrs['class'] = 'form-control select2'
            # field.widget.attrs['data-live-search'] = 'true'
            # field.widget.attrs['data-provide'] = 'selectpicker'
            # field.widget.attrs['data-size '] = '10'
        elif field and isinstance(field, forms.ChoiceField):
            field.widget.attrs['class'] = 'form-control selectgroup w-100'
        elif field and isinstance(field, forms.BooleanField):
            field.widget.attrs['class'] = 'form-control selectgroup w-100 mr-2'
            field.widget.attrs['data-on'] = 'Sim'
            field.widget.attrs['data-off'] = 'Não'
            field.widget.attrs['data-toggle'] = 'toggle'
            field.widget.attrs['data-onstyle'] = 'success'
            field.widget.attrs['data-offstyle'] = 'danger'
        elif field and isinstance(field, forms.ModelMultipleChoiceField):
            pass
            # field.widget.attrs['class'] = 'selectpicker form-control'
            # field.widget.attrs['data-live-search'] = 'true'
            # field.widget.attrs['data-provide'] = 'selectpicker'
            # field.widget.attrs['data-size '] = '10'
            # field.widget.attrs['multiple'] = 'true'
        elif field and isinstance(field, forms.DateField):
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['id'] = 'datepicker'
            field.widget.attrs['name'] = 'datepicker'
        elif field and isinstance(field, forms.DateTimeField):

            field.widget.attrs['data-provide'] = 'datepicker2'
            field.widget.attrs['class'] = 'form-control datepicker2'
        elif field and isinstance(field, forms.TimeField):
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['id'] = 'timepicker'
            field.widget.attrs['name'] = 'timepicker'
        elif field and isinstance(field, forms.CharField):
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['style'] = 'text-transform:uppercase'
            if field_name is not 'usuario':
                field.widget.attrs['onkeyup'] = 'this.value = this.value.toUpperCase()'
            # field.widget.attrs['data-show-meridian'] = 'false'
        # elif field and isinstance(field, forms.BooleanField):
        #     field.widget.attrs['class'] = 'custom-control-input'
        else:
            pass
            field.widget.attrs['class'] = 'form-control'
        if field.required:
            field.label = field.label + '*'
        else:
            field.label = field.label



def get_user_type(user):
    if user.is_superuser:
        return user
    from core.modulos.user_profile.user_profile import UserProfile
    if UserProfile.objects.filter(user=user).exists():
        return user.userProfile
    from core.modulos.profissional.profissional import Profissional
    if Profissional.objects.filter(user=user).exists():
        return user.userProfissional
    from core.modulos.atendente.atendente import Atendente
    if Atendente.objects.filter(user=user).exists():
        return user.userAtendente
    from core.modulos.cliente.cliente import Cliente
    if Cliente.objects.filter(user=user).exists():
        return user.userCliente





class MyListViewSearcheGeneric(SearchableListMixin):
    COLUMNS = []

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        q = self.request.GET.get("q", "").strip()
        context['q'] = q
        context['COLUMNS'] = self.COLUMNS
        return context

class MyLabls(object):
    NAME_MODEL = None
    NAME_MODEL_PLURAL = None
    PAGE_CREATE_VIEW = None
    PAGE_UPDATE_VIEW = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['labels'] = LabesProperty
        context['NAME_MODEL'] = self.NAME_MODEL
        context['NAME_MODEL_PLURAL'] = self.NAME_MODEL_PLURAL
        context['PAGE_CREATE_VIEW'] = self.PAGE_CREATE_VIEW
        context['PAGE_UPDATE_VIEW'] = self.PAGE_UPDATE_VIEW
        context['SAVE_MODEL'] = None

        save_model = self.request.session.pop('save_model', None)
        if save_model:
            context['SAVE_MODEL'] = True
        edit_model = self.request.session.pop('update_model', None)
        if edit_model:
            context['SAVE_MODEL'] = False

        return context

class UpperCaseCharField(models.CharField):
    def __init__(self, *args, **kwargs):
        super(UpperCaseCharField, self).__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        value = getattr(model_instance, self.attname, None)
        if value:
            value = value.upper()
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super(UpperCaseCharField, self).pre_save(model_instance, add)

#
#
# def createPathPhotoHealthTips(instance, filename):
#     directory = 'health_tips/' + str(instance.id)
#     full_path = str(directory) + "/%s" % (filename)
#     return full_path
#
#
#
# def createPathPhotoLogPost(instance, filename):
#     directory = 'blog_post/' + str(instance.id)
#     full_path = str(directory) + "/%s" % (filename)
#     return full_path
