# Generated by Django 5.0.4 on 2024-05-02 11:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_alter_genre_name_alter_movie_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='mpaaRating',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='movies.mpaarating'),
        ),
    ]
