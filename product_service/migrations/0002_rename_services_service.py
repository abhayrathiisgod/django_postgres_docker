# Generated by Django 5.0.4 on 2024-04-25 06:13

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("product_service", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="SERVICES",
            new_name="SERVICE",
        ),
    ]