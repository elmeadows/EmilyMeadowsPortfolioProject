from django.db import migrations


def add_campus_skillswap(apps, schema_editor):
    Project = apps.get_model("hello", "Project")
    Project.objects.update_or_create(
        title="Campus Skillswap",
        defaults={
            "description": (
                "A Python Django web app for a job board fostering community "
                "and enabling college students to provide and receive help "
                "where needed."
            ),
            "technologies": "Python, Django, SQLite, Claude, Gemini, Codex",
            "image_url": "/static/hello/campus-skillswap-home.png",
            "project_url": "",
            "github_url": "https://github.com/elmeadows/campus_skillswap.git",
        },
    )


def remove_campus_skillswap(apps, schema_editor):
    Project = apps.get_model("hello", "Project")
    Project.objects.filter(title="Campus Skillswap").delete()


class Migration(migrations.Migration):

    dependencies = [
        ("hello", "0002_project_delete_logmessage"),
    ]

    operations = [
        migrations.RunPython(add_campus_skillswap, remove_campus_skillswap),
    ]
