# Generated by Django 5.0.3 on 2024-03-24 18:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0008_remove_projectstable_bids_projectstable_bids"),
    ]

    operations = [
        migrations.AddField(
            model_name="bidstable",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="bid_created_by",
                to="app.profilestable",
            ),
        ),
        migrations.AlterField(
            model_name="projectstable",
            name="bids",
            field=models.ManyToManyField(
                blank=True, related_name="bids", to="app.bidstable"
            ),
        ),
    ]