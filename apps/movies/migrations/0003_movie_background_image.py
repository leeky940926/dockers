# Generated by Django 3.2 on 2022-06-18 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20220521_0623'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='background_image',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
