from django.db import migrations


def add_media_generation(apps, schema_editor):
    Project = apps.get_model("hello", "Project")
    Project.objects.update_or_create(
        title="Media Generation",
        defaults={
            "description": "Limited time media generation from prompts in Google Flow.",
            "technologies": "Google Flow, Nano Banana",
            "image_url": "/static/hello/media-generation.png",
            "project_url": "",
            "github_url": "",
        },
    )


def remove_media_generation(apps, schema_editor):
    Project = apps.get_model("hello", "Project")
    Project.objects.filter(title="Media Generation").delete()


class Migration(migrations.Migration):

    dependencies = [
        ("hello", "0004_add_learning_log_project"),
    ]

    operations = [
        migrations.RunPython(add_media_generation, remove_media_generation),
    ]
