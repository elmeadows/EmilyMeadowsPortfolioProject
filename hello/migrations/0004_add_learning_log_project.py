from django.db import migrations


def add_learning_log(apps, schema_editor):
    Project = apps.get_model("hello", "Project")
    Project.objects.update_or_create(
        title="Learning Log",
        defaults={
            "description": (
                "A Python Django web app creating a virtual log of new topics "
                "or hobbies learned."
            ),
            "technologies": "Python, Django, Bootstrap4, Gunicorn",
            "image_url": "/static/hello/learning-log-home.png",
            "project_url": "",
            "github_url": "https://github.com/elmeadows/learning_log.git",
        },
    )


def remove_learning_log(apps, schema_editor):
    Project = apps.get_model("hello", "Project")
    Project.objects.filter(title="Learning Log").delete()


class Migration(migrations.Migration):

    dependencies = [
        ("hello", "0003_add_campus_skillswap_project"),
    ]

    operations = [
        migrations.RunPython(add_learning_log, remove_learning_log),
    ]
