import os

from django import forms
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
from extra_views import SearchableListMixin

from core.util.labels_property import LabesProperty


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
            # field.widget.attrs['data-show-meridian'] = 'false'
        # elif field and isinstance(field, forms.BooleanField):
        #     field.widget.attrs['class'] = 'custom-control-input'
        else:
            pass
            field.widget.attrs['class'] = 'form-control'
        if field.required:
            field.label = field.label + '*'


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


from django.db import models
from six import with_metaclass


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
