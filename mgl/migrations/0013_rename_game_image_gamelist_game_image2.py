# Generated by Django 5.1.2 on 2024-10-18 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mgl', '0012_gamelist_hours_taken'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gamelist',
            old_name='game_image',
            new_name='game_image2',
        ),
    ]
