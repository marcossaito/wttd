# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Speaker(models.Model):
	
	name = models.CharField(_('Nome'), max_length=255)
	slug = models.SlugField(_('Slug'))
	url = models.URLField(_('Url'))
	description = models.TextField(_(u'Descrição'), blank=True)

	def __unicode__(self):
		return self.name

class Contact(models.Model):
	KIND = (('P',_('telefone')),
			('E',_('E-MAIL')),
			('F',_('Fax')),
		)

	speaker = models.ForeignKey(Speaker, verbose_name=_('palestrante'))
	kind = models.CharField(_('tipo'), max_length=1, choices=KIND)
	value = models.CharField(_('valor'), max_length=255)