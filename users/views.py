#!/usr/bin/env python

from django.shortcuts import render, redirect
from django.core.context_processors import csrf
from django.contrib.auth import *
from django.contrib.auth.forms import UserCreationForm 
#def staff(request):
#    '''
#    login1
#    '''
#    if request.POST:
#        username = password = ''
#        username = request.POST.get('username')
#        password = request.POST.get('password')
#        user     = authenticate(username=username, password=password)
#        if user is not None and user.is_active:
#                login(request, user)
#                return redirect('/')
#    ctx = {}
#    ctx.update(csrf(request))
#    return render(request, 'login.html',ctx)
def staff(request): 
    if request.method == 'POST': 
        form = UserCreationForm(request.POST) 
        if form.is_valid(): 
            new_user = form.save() 
        return redirect("/") 
    else:
        form = UserCreationForm()
        ctx = {'form': form}
        ctx.update(csrf(request))       
        return render(request, "users.html", ctx)
