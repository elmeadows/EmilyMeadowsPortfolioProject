from django.db import migrations


def add_social_media_project(apps, schema_editor):
    Project = apps.get_model("hello", "Project")
    Project.objects.update_or_create(
        title="Adventurers Social Media Project",
        defaults={
            "description": "Social network for people who enjoy outdoor activities and being outside.",
            "technologies": "Python, Django",
            "image_url": "/static/hello/social_media_image.png",
            "project_url": "",
            "github_url": "",
        },
    )


def remove_social_media_project(apps, schema_editor):
    Project = apps.get_model("hello", "Project")
    Project.objects.filter(title="Adventurers Social Media Project").delete()


class Migration(migrations.Migration):

    dependencies = [
        ("hello", "0008_add_n8n_agent_workflow_project"),
    ]

    operations = [
        migrations.RunPython(add_social_media_project, remove_social_media_project),
    ]
