from django.db import migrations


def add_n8n_agent_workflow(apps, schema_editor):
    Project = apps.get_model("hello", "Project")
    Project.objects.update_or_create(
        title="n8n Agent Workflow Project",
        defaults={
            "description": "Workflow for processing maintenance requests for a Handyman business.",
            "technologies": "n8n Cloud, Google Gemini, JavaScript",
            "image_url": "/static/hello/n8n-agent-workflow.png",
            "project_url": "",
            "github_url": "",
        },
    )


def remove_n8n_agent_workflow(apps, schema_editor):
    Project = apps.get_model("hello", "Project")
    Project.objects.filter(title="n8n Agent Workflow Project").delete()


class Migration(migrations.Migration):

    dependencies = [
        ("hello", "0007_add_langchain_agent_project"),
    ]

    operations = [
        migrations.RunPython(add_n8n_agent_workflow, remove_n8n_agent_workflow),
    ]
