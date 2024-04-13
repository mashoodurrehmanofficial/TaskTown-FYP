# Generated by Django 5.0.3 on 2024-03-24 10:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0006_alter_projectstable_end_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="projectstable",
            name="bids",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="bids",
                to="app.bidstable",
            ),
        ),
        migrations.AlterField(
            model_name="projectstable",
            name="status",
            field=models.CharField(
                choices=[
                    ("Open", "Open"),
                    ("Active", "Active"),
                    ("Disputed", "Disputed"),
                    ("Completed", "Completed"),
                ],
                default="",
                max_length=1000,
            ),
        ),
    ]
