# Generated by Django 3.2 on 2022-05-21 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=None)),
                ('deleted_at', models.DateTimeField(default=None)),
                ('title', models.CharField(max_length=100)),
                ('year', models.PositiveIntegerField()),
                ('rating', models.DecimalField(decimal_places=2, max_digits=5)),
                ('runtime', models.PositiveIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=None)),
                ('deleted_at', models.DateTimeField(default=None)),
                ('title', models.CharField(max_length=40)),
                ('content', models.TextField()),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
