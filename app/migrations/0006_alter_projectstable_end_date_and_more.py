# Generated by Django 5.0.3 on 2024-03-24 09:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0005_remove_experiencetable_time_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="projectstable",
            name="end_date",
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name="projectstable",
            name="start_date",
            field=models.DateField(blank=True),
        ),
    ]
