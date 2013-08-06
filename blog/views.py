#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response, redirect, RequestContext, render
from blog.models import Reply, Blog, UserProfile
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django import forms
import datetime

class RF(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()

class LF(forms.Form):
    username = forms.CharField(label='用户名')
    password = forms.CharField(label='密码',widget=forms.PasswordInput)

class BF(forms.ModelForm):
    class Meta:
	model = Blog
	fields = ['title','type','content','digest','picture']

def index(request):
    return render_to_response('blog.html',locals(),context_instance=RequestContext(request))

def regist(request):
    if request.method == "POST":
        rf = RF(request.POST)
        if rf.is_valid():
            username = rf.cleaned_data['username']
            password = rf.cleaned_data['password']
            email = rf.cleaned_data['email']
            User.objects.create_user(username, email, password) 
	    return HttpResponseRedirect('/login/')
    else :
        rf = RF()
    return render_to_response('registe.html', {'rf':rf})

def user_login(request):
    if request.method == "POST" :
	lf = LF(request.POST)
	if lf.is_valid():
	    username = lf.cleaned_data['username']
	    password = lf.cleaned_data['password']
	    user = authenticate(username=username, password=password) 

	    if user is not None:
		login(request, user)
		return HttpResponseRedirect('/index/') 
    else:
	lf=LF()
    return render_to_response('login.html',{'lf':lf}) 

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def write(request):
    author = request.user
    pub_date = datetime.datetime.now()
    if request.method == "POST":
	bforms = BF(request.POST)
	if bf.is_valid():
	    title = bforms.cleaned_data['title']
	    type  = bforms.cleaned_data['type']
	    digest = bforms.cleaned_data['digest']
	    content = bforms.cleaned_data['content']
	    picture = bforms.cleaned_data['picture']
	    bf = BF.objects.create(title=title, type=type, digest=digest, content=content, picture=picture, author=author, pubt_date=pub_date)
	    bf.save()
    else:
	bforms = BF()
    return render_to_response('write_blog.html', {'bforms':bforms}, context_instance=RequestContext(request))
