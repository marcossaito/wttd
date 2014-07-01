# coding: utf-8
from django.test import TestCase
from datetime import datetime
from eventex.subscriptions.models import Subscription

class SubscriptionTest(TestCase):
	
	def setUp(self):
		self.obj = Subscription(
				name = 'Marcos Saito',
				cpf = '12345678901',
				email = 'marcos@saito.net',
				phone = '21-96186190'
			)
	
	def test_create(self):
		'Subscription must have name, cpf, email, phone'
		self.obj.save()
		self.assertEqual(1, self.obj.id)

	def test_has_created_at(self):
		'Subscription must have atomatic created_at.'
		self.obj.save()
		self.assertIsInstance(self.obj.created_at, datetime)

	def test_unicode(self):
		self.assertEqual(u'Marcos Saito', unicode(self.obj	))