# Generated by Django 5.0.3 on 2024-03-23 09:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0002_profilestable_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profilestable",
            name="username",
            field=models.CharField(default="", max_length=1000),
        ),
    ]
