# Generated by Django 4.2.1 on 2023-05-27 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("teams", "0009_card"),
    ]

    operations = [
        migrations.DeleteModel(name="Card",),
    ]
