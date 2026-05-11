import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail
from hello.forms import ProjectForm, ContactForm
from hello.models import Project
from django.views.generic import ListView, DetailView


class HomeListView(ListView):
    """Renders the home page, with a list of featured projects."""
    model = Project
    context_object_name = "project_list"
    template_name = "hello/home.html"

    def get_queryset(self):
        return Project.objects.all()[:3]  # Show 3 most recent projects

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

def about(request):
    return render(request, "hello/about.html")

class ProjectDetailView(DetailView):
    """Renders the individual project detail page."""
    model = Project
    template_name = "hello/project_detail.html"
    context_object_name = "project"

def skills(request):
    """Renders the skills page."""
    return render(request, "hello/skills.html")

def resume(request):
    """Renders the resume page."""
    return render(request, "hello/resume.html")

def contact(request):
    """Renders the contact page."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Send the email
            subject = f"New Contact Form Submission from {name}"
            body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            send_mail(
                subject,
                body,
                email, # From email (using user's email might be rejected by some SMTP servers, but we'll use it as from_email for simplicity, or configure DEFAULT_FROM_EMAIL)
                ['meadowselm@gmail.com'], # To email
                fail_silently=False,
            )
            
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()
        
    return render(request, "hello/contact.html", {'form': form})

def projects(request):
    """Renders the projects portfolio page."""
    project_list = Project.objects.all()
    context = {"project_list": project_list}
    return render(request, "hello/projects.html", context)
