from django.db import migrations


def add_langchain_agent(apps, schema_editor):
    Project = apps.get_model("hello", "Project")
    Project.objects.update_or_create(
        title="LangChain Agent Project",
        defaults={
            "description": "Basic development of AI agent using Python and LangChain.",
            "technologies": "Python, LangChain, Google Gemini",
            "image_url": "/static/hello/langchain-agent-project.png",
            "project_url": "",
            "github_url": "",
        },
    )


def remove_langchain_agent(apps, schema_editor):
    Project = apps.get_model("hello", "Project")
    Project.objects.filter(title="LangChain Agent Project").delete()


class Migration(migrations.Migration):

    dependencies = [
        ("hello", "0006_add_media_generation_project"),
    ]

    operations = [
        migrations.RunPython(add_langchain_agent, remove_langchain_agent),
    ]
