# Generated by Django 5.0.7 on 2024-07-23 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mgl', '0008_alter_gamelist_about_alter_gamelist_other'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamelist',
            name='about',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]