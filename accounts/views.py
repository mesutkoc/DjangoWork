# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from .form import LoginForm,RegisterForm,EditProfile
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from ManageYourself.models import *

home_page = None

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password )
        login(request, user)
        return redirect('project')
    return render(request,'login.html',{'form':form})

def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        mail = form.cleaned_data.get('mail')
        password = form.cleaned_data.get('password1')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username,mail=mail,password=password)
        login(request,new_user)
        return redirect('project')
    return render(request, 'register.html', {'form': form})

def edit_view(request):
    oldUserName=request.user.username
    if request.method =='POST':
        form = EditProfile(request.POST or None, instance=request.user)
        if form.is_valid():
            form.save()
            newUserName = request.user.username
            UserProjects.objects.filter(Username=oldUserName).update(Username=newUserName)
            return redirect('project')
    else:
        form = EditProfile(instance=request.user)
        return render(request, 'rename.html', {'form': form})

def editpassword_view(request):
    if request.method =='POST':
        form = PasswordChangeForm(data=request.POST or None, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('project')
        else:
            return redirect('/accounts/editpassword')
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request, 'updatepassword.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('accounts:login')