# coding: utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _

class Subscription(models.Model):
	name = models.CharField(_('Nome'), max_length=100)
	cpf = models.CharField(_('CPF'), max_length=11, unique=True)
	email = models.EmailField(_('Email'), unique=True)
	phone = models.CharField(_('Telefone'), max_length=20, blank=True)
	created_at = models.DateTimeField(_('Criado em'), auto_now_add=True)
	paid = models.BooleanField(_('Pago'))

	class Meta:
		ordering = ['created_at']
		verbose_name = ('inscrição')
		verbose_name_plural = ('inscrições')

	def __unicode__(self):
		return self.name