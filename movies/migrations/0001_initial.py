# Generated by Django 5.0.4 on 2024-04-30 14:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='MPAARating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('duration', models.IntegerField()),
                ('language', models.CharField(max_length=100)),
                ('userRating', models.CharField(max_length=10)),
                ('genre', models.ManyToManyField(related_name='genre', to='movies.genre')),
                ('mpaaRating', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating', to='movies.mpaarating')),
            ],
        ),
    ]
