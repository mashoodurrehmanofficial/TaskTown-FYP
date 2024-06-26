# Generated by Django 5.0.3 on 2024-05-15 11:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0016_remove_disputestable_messages_projectstable_messages"),
    ]

    operations = [
        migrations.AddField(
            model_name="projectstable",
            name="admin",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="administrator",
                to="app.profilestable",
            ),
        ),
        migrations.AddField(
            model_name="projectstable",
            name="is_disputed",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
