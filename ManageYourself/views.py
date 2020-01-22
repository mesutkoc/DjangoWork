# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import *

from .forms import *
from django.contrib.auth.models import User

def mainpage(request):
    return render(request,'Navbar.html')

def projectview(request):
    projects = Projects.objects.all().filter(userprojects__Username=request.user.username)
    return render(request,'ProjectView.html',{'Projectss':projects})

def project_create(request):
    if request.method == "POST":
        form = postForm(request.POST)
        if form.is_valid():
            p = UserProjects.objects.create(Username=request.user.username, Project_NameUser=form.save())
            p.save()
            postprojectname = form.save()
            return redirect('project')

    else:
        form = postForm()
    form = postForm()
    context = {
        'form': form,
    }
    return render(request,'CreateProje.html',context)

def project_update(request,id):
    posts = get_object_or_404(Projects, id=id)
    form = postForm(request.POST or None, instance=posts)
    if form.is_valid():
        form.save()
        return redirect('project')
    context = {
        'form': form,
    }
    return render(request, 'UpdateProject.html', context)

def project_delete(request, id=None):
    post= get_object_or_404(Projects, id=id)
    postlar = Post.objects.all().filter(Project_NamePost=get_object_or_404(Projects,id=id))
    users = UserProjects.objects.filter(Project_NameUser=get_object_or_404(Projects,id=id))
    # for i in postlar:
    #     print i
    # for i in users:
    #     print i
    postlar.delete()
    users.delete()
    post.delete()
    return redirect('project')

def project_leave(request,id=None):
    post = get_object_or_404(Projects,id=id)
    projects = UserProjects.objects.filter(Username=request.user.username ,Project_NameUser=post)
    projects.delete()
    return redirect('project')

def project_completed(request,id=None):
    project = get_object_or_404(Projects, id=id)
    posts = Post.objects.all().filter(Project_NamePost=project)
    users = UserProjects.objects.filter(Project_NameUser=project)
    posts.delete()
    users.delete()
    project.delete()
    return redirect('project')

def project_posts(request,id=None):
    Projectname = Projects.objects.filter(ProjectName=get_object_or_404(Projects,id=id))
    posts = Post.objects.filter(Project_NamePost=get_object_or_404(Projects,id=id))
    user = UserProjects.objects.filter(Project_NameUser_id=Projectname)
    return render(request,'ProjectPost.html',{'Posts':posts,'Users':user,'Projectname':Projectname})


def enroll_user(request):
    if request.method == 'POST':
        form = postForm3(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('project')
    else:
        form = postForm3()
    form = postForm3()
    context = {
        'form': form,
    }
    return render(request,'EnrollUser.html',context)

def post_create(request):
    if request.method == "POST":
        form = postForm2(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('project')
    else:
        form = postForm2()
    form = postForm2()
    context = {
        'form': form,
    }
    return render(request,'CreatePost.html',context)

def post_update(request,id=None):
    posts = get_object_or_404(Post, id=id)
    form = postForm2(request.POST or None, instance=posts)
    if form.is_valid():
        form.save()
        return redirect('project')
    context = {
        'form': form,
    }
    return render(request, 'CreatePost.html', context)


def post_delete(request,id=None):
    posts = get_object_or_404(Post, id=id)
    posts.delete()
    return redirect('project')
