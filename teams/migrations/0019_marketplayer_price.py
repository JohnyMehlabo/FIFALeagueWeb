# Generated by Django 4.2.1 on 2023-06-03 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("teams", "0018_marketplayer_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="marketplayer",
            name="price",
            field=models.FloatField(default=10),
            preserve_default=False,
        ),
    ]