# Generated by Django 5.0.3 on 2024-04-27 07:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0013_rename_checkout_session_id_profilestable_stripe_customer_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="profilestable",
            name="image_path",
            field=models.CharField(default="", max_length=1000),
        ),
    ]