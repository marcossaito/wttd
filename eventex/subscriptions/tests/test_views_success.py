from django.test import TestCase
from eventex.subscriptions.models import Subscription

class SucessTest(TestCase):
	def setUp(self):
		s = Subscription.objects.create(name='Marcos Saito', cpf='12345678901', 
										email='marcos@net.com', phone='34-33334035', paid=False)
		self.resp = self.client.get('subscriptions:success', args=[s.pk])

	def test_get(self):
		'GET /inscricao/1/ should return status code 200.'
		self.assertEqual(200, self.resp.status_code)