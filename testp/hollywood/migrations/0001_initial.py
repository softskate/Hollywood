# Generated by Django 3.2.9 on 2021-11-10 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor_id', models.IntegerField(unique=True, verbose_name='ID актера')),
                ('name', models.CharField(max_length=100, verbose_name='Имя актера')),
            ],
        ),
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writer_id', models.IntegerField(unique=True, verbose_name='ID сценариста')),
                ('name', models.CharField(max_length=100, verbose_name='Имя сценариста')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.IntegerField(unique=True, verbose_name='ID фильма')),
                ('title', models.CharField(max_length=200, verbose_name='Название фильма')),
                ('imdb_rating', models.FloatField(verbose_name='Рейтинг фильма')),
                ('genre', models.TextField(verbose_name='Жанры')),
                ('description', models.TextField(verbose_name='Описание фильма')),
                ('writers_names', models.TextField(verbose_name='Имя сценариста')),
                ('director', models.CharField(max_length=100, verbose_name='Режиссер')),
                ('actors_names', models.TextField(verbose_name='Список имен, разделенных запятыми')),
                ('actors', models.ManyToManyField(blank=True, to='hollywood.Actor', verbose_name='ID актера')),
                ('writers', models.ManyToManyField(blank=True, to='hollywood.Writer', verbose_name='ID сценариста')),
            ],
        ),
    ]
