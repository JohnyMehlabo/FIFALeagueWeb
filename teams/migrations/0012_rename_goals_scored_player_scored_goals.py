# Generated by Django 4.2.1 on 2023-05-28 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("teams", "0011_player_goals_scored_player_saves"),
    ]

    operations = [
        migrations.RenameField(
            model_name="player", old_name="goals_scored", new_name="scored_goals",
        ),
    ]