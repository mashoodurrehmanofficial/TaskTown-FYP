# Generated by Django 5.0.3 on 2024-03-24 18:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0009_bidstable_created_by_alter_projectstable_bids"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bidstable",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="app.profilestable",
            ),
        ),
    ]
