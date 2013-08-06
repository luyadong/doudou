from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response, redirect, RequestContext
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render_to_response('index.html', locals(), context_instance=RequestContext(request))

def contacts(request):
    return render_to_response('contacts.html',locals(), context_instance=RequestContext(request))
