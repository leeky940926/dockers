# Generated by Django 2.2.16 on 2022-11-13 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('last_password_changed_at', models.DateTimeField(null=True)),
                ('last_visit', models.DateTimeField(null=True)),
            ],
        ),
    ]
