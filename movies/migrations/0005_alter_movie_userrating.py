# Generated by Django 5.0.4 on 2024-05-02 12:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_alter_movie_mpaarating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='userRating',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(5)]),
        ),
    ]
