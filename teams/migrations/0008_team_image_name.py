# Generated by Django 4.2.1 on 2023-05-27 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("teams", "0007_alter_team_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="team",
            name="image_name",
            field=models.CharField(default="a", max_length=30),
            preserve_default=False,
        ),
    ]
