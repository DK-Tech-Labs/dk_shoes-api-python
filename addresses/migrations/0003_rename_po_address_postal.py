# Generated by Django 4.2 on 2023-06-19 19:53

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("addresses", "0002_alter_address_complement"),
    ]

    operations = [
        migrations.RenameField(
            model_name="address",
            old_name="po",
            new_name="postal",
        ),
    ]
