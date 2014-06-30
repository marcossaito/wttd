# coding: utf-8

from django import forms
from django.utils.translation import gettext

class SubscriptionForm(forms.Form):
	name  = forms.CharField(label=gettext('Nome'))
	cpf   = forms.CharField(label=gettext('CPF'))
	email = forms.EmailField(label=gettext('Email'))
	phone = forms.CharField(label=gettext('Telefone'))