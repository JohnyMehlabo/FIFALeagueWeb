# Generated by Django 4.2.1 on 2023-05-31 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("teams", "0016_marketplayer_marketkeeper"),
    ]

    operations = [
        migrations.AddField(
            model_name="marketplayer",
            name="speed_stat_max",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
