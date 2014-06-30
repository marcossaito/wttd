# coding: utf-8
# Create your views here.

'''Para usar um HttpResponse simples como return'''
#from django.http import HttpResponse
from django.views.generic.simple import direct_to_template
from eventex.subscriptions.forms import SubscriptionForm

def subscribe(request):
	return direct_to_template(request, 'subscriptions/subscription_form.html', {'form':SubscriptionForm()})