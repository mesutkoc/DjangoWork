from django import forms
from django.http import request

from .models import *
from django.contrib.auth.models import User


class postForm(forms.ModelForm):
    class Meta:
        model = Projects

        fields = [
            'ProjectName'
        ]

class postForm2(forms.ModelForm):
    STATUS_CHOICES = (
        (1, ("TO DO")),
        (2, ("DOING")),
        (3, ("DONE")),
    )
    Status = forms.ChoiceField(choices=STATUS_CHOICES)

    class Meta:
        model = Post

        fields = [
            'Work',
            'Content',
            'Worker',
            'Project_NamePost',
            'Status'
        ]

class postForm3(forms.ModelForm):

    class Meta:
        model = UserProjects
        fields = (
            'Username',
            'Project_NameUser'
        )