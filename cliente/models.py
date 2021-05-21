from django import forms
from django.db import models


class ContactForm(forms.Form):
	name = forms.CharField(max_length = 50)
	email = forms.EmailField(max_length = 150)

class Contact(models.Model):
    class Meta:
        verbose_name = 'CONTATO'
        verbose_name_plural = 'CONTATOS'
    name = models.CharField(max_length=50)
    email = models.EmailField()
    lido = models.BooleanField(default=False)
    
    def __str__(self):
        if self.lido:
            return self.name