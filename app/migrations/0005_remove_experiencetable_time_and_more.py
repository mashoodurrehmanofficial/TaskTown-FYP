# Generated by Django 5.0.3 on 2024-03-23 10:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0004_profilestable_password"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="experiencetable",
            name="time",
        ),
        migrations.AlterField(
            model_name="experiencetable",
            name="end_date",
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name="experiencetable",
            name="start_date",
            field=models.DateField(blank=True),
        ),
    ]
