# coding: utf-8
from django import forms
from django.core.exceptions import ValidationError
from .models import _, Person


class PersonForm(forms.ModelForm):

    class Meta:
        model = Person

    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)

        self.fields['kind'].widget = forms.HiddenInput()
        self.fields['cpf'].validators.append(self.cpf_validator)

    def cpf_validator(value):
        if not value.isdigit():
            raise ValidationError(_(u'CPF deve conter apenas números.'))

        if not len(value) is 11:
            raise ValidationError(_(u'CPF deve conter 11 dígitos.'))


class FormLogin(forms.Form):
    cpf = forms.CharField(label=_('CPF'))
    email = forms.EmailField(label=_('E-mail'))
