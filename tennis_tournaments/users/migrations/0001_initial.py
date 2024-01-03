# Generated by Django 5.0.1 on 2024-01-03 19:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=128)),
                ('password', models.CharField(max_length=128)),
                ('First_name', models.CharField(max_length=30)),
                ('Second_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('balance', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='sessions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time_sessions', models.DateTimeField()),
                ('end_time_sessions', models.DateTimeField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
        migrations.CreateModel(
            name='basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prise_bid', models.FloatField(default=0)),
                ('coaf_bid', models.FloatField(default=0)),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.game')),
                ('user_if', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
    ]