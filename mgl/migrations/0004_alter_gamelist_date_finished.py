# Generated by Django 5.0.7 on 2024-07-17 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mgl', '0003_alter_gamelist_date_finished'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamelist',
            name='date_finished',
            field=models.CharField(blank=True, default='???', max_length=10),
        ),
    ]
