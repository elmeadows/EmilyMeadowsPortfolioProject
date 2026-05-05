from django import forms

from hello.models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ("title", "description", "technologies", "image_url", "project_url", "github_url")
