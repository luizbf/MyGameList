# Generated by Django 5.1.2 on 2024-10-18 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mgl', '0011_alter_gamelist_game_image_alter_gamelist_game_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamelist',
            name='hours_taken',
            field=models.CharField(blank=True, default='???', max_length=15),
        ),
    ]