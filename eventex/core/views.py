# coding: utf-8

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic.simple import direct_to_template

def homepage(request):
	'''
		Processa o context processors, injeta no context coisas que são muito usadas
		
	'''
	context = RequestContext(request)
	return render_to_response('index.html', context)

def speaker_detail(request, slug):
	speaker = get_object_or_404(Speaker, slug=slug)
	context = {'speaker': speaker}
	return render_to_response(request, 'core/speaker_detail.html',context)

''' Codigo para usar Tamplates Variables como 'STATIC_URL' '''
#from django.shortcuts import render_to_response
#from django.conf import settings
#
#def homepage(request):
#	context = {'STATIC_ULR': settings.STATIC_ULR}
#	return render_to_response('index.html',context)

''' Código q renderiza na mão um tamplate '''
#from django.http import HttpResponse
#from django.template import loader, Context

#def homepage(request):
#	t = loader.get_template('index.html')
#	# não retorna o conteudo da classe template, mas uma instancia de template
#	c = Context()
#
#	content = t.render(c)
#
#	return HttpResponse(content)