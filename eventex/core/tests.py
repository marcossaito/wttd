# coding: utf-8

"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.core.urlresolvers import reverse as r

class HomepageTest(TestCase):
    
    def setUp(self):
    	self.resp = self.client.get(r('core:homepage'))

    def get_test(self):
    	'GET / must return status code 200.'
    	self.assertEquals(200, self.resp.status_code)

    def test_template(self):
    	'Homepage must use tamplate index.html'
    	self.assertTemplateUsed(self.resp, 'index.html')