from django import forms
from django.db import models


class ContactForm(forms.Form):
	name = forms.CharField(max_length = 50)
	email = forms.EmailField(max_length = 150)

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    lido = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def __str__(self):
        return self.name