# Generated by Django 5.1.1 on 2024-09-24 11:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("entries", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task",
            options={"ordering": ["due_by"]},
        ),
        migrations.AlterField(
            model_name="task",
            name="priority",
            field=models.IntegerField(
                choices=[(1, "Low"), (2, "Medium"), (3, "High")], default=1
            ),
        ),
    ]
