from django.db import models
from django.utils import timezone

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=300, help_text="Comma-separated list of technologies")
    image_url = models.URLField(blank=True, null=True)
    project_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    created_date = models.DateTimeField("date created", auto_now_add=True)
    updated_date = models.DateTimeField("date updated", auto_now=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        """Returns a string representation of a project."""
        return self.title
