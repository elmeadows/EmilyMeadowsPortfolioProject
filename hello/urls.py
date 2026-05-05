from django.urls import path
from hello import views
from hello.models import Project

home_list_view = views.HomeListView.as_view(
    queryset=Project.objects.all()[:3],  # :3 limits the results to the three most recent
    context_object_name="project_list",
    template_name="hello/home.html",
)

urlpatterns = [
    path("", home_list_view, name="home"),
    path("about/", views.about, name="about"),
    path("projects/", views.projects, name="projects"),
    path("projects/<int:pk>/", views.ProjectDetailView.as_view(), name="project_detail"),
    path("skills/", views.skills, name="skills"),
    path("resume/", views.resume, name="resume"),
    path("contact/", views.contact, name="contact"),
]
