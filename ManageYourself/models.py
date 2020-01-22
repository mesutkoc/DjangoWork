# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Projects(models.Model):
    ProjectName = models.CharField(max_length=100)
    PublishedDate = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return "/ManageYourself/{}".format(self.id)
    def __str__(self):
        return self.ProjectName

class UserProjects(models.Model):
    Username = models.CharField(max_length=100)
    Project_NameUser = models.ForeignKey(Projects, on_delete=Projects)
    def __str__(self):
        return self.Username

class Post(models.Model):
    Work = models.CharField(max_length=100)
    Content = models.CharField(max_length=200)
    PublishedDate_Post = models.DateTimeField(auto_now_add=True)
    Worker = models.CharField(max_length=100)
    Project_NamePost = models.ForeignKey(Projects, on_delete=models.CASCADE)
    Status = models.CharField(max_length=100)
    def __str__(self):
        return self.Work