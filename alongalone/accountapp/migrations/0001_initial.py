# Generated by Django 4.0.6 on 2022-08-16 19:13

import accountapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nickname', models.CharField(blank=True, max_length=20)),
                ('profilePhoto', models.ImageField(default='accountapp/static/img/default_user.png', upload_to=accountapp.models.profilePhoto_path)),
                ('mainCategory', models.CharField(choices=[('b', '혼밥'), ('s', '혼술'), ('c', '혼카페')], default='b', max_length=100)),
                ('introduction', models.CharField(blank=True, max_length=100)),
                ('cash', models.PositiveIntegerField(default=0)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]