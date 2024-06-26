# Generated by Django 5.0.4 on 2024-04-30 16:54

import django.db.models.functions.text
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_genre_name_alter_mpaarating_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(help_text='Enter movie genre', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(upload_to='assets/images/'),
        ),
        migrations.AddConstraint(
            model_name='genre',
            constraint=models.UniqueConstraint(django.db.models.functions.text.Lower('name'), name='genre_name_case_insensitive_unique', violation_error_message='Genre already exists (case insensitive match)'),
        ),
    ]
