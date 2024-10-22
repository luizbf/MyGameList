# Generated by Django 5.0.7 on 2024-07-17 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_name', models.CharField(max_length=255)),
                ('date_finished', models.DateField(default='???')),
                ('about', models.TextField(blank=True)),
                ('other', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Game list',
                'verbose_name_plural': 'Game list',
            },
        ),
    ]