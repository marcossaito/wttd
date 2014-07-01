# coding: utf-8
# Create your views here.

'''Para usar um HttpResponse simples como return'''
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic.simple import direct_to_template
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription
	
def subscribe(request):
	if request.method == 'POST':
		form = SubscriptionForm(request.POST)

		if not form.is_valid():	
			return direct_to_template(request,'subscriptions/subscription_form.html',{'form': form})
			
		obj = form.save()
		return HttpResponseRedirect('/inscricao/%d/' % obj.pk)
	
	else:
		form = SubscriptionForm()	

	return direct_to_template(request,'subscriptions/subscription_form.html',{'form': form})

def new(request):
	return direct_to_template(request, 'subscriptions/subscription_form.html',{'form': SubscriptionForm()})

def create(request):
	form = SubscriptionForm(request.POST)

	if not form.is_valid():
		return direct_to_template(request, 'subscriptions/subscription_form.html',{'form': form})

	obj = form.save()
	return HttpResponseRedirect('/inscricao/%d/' % obj.pk)

def success(request,pk):
	subscription = get_object_or_404(Subscription, pk=pk)
	return direct_to_template(request,'subscriptions/subscription_detail.html',{'subscription': subscription})