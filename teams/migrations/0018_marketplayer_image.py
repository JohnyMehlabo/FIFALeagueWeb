# Generated by Django 4.2.1 on 2023-05-31 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("teams", "0017_marketplayer_speed_stat_max"),
    ]

    operations = [
        migrations.AddField(
            model_name="marketplayer",
            name="image",
            field=models.CharField(default="", max_length=40),
            preserve_default=False,
        ),
    ]
