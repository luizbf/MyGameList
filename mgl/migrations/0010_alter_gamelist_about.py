# Generated by Django 5.0.7 on 2024-07-23 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mgl', '0009_alter_gamelist_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamelist',
            name='about',
            field=models.TextField(blank=True),
        ),
    ]