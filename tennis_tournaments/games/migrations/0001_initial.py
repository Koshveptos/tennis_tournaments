# Generated by Django 5.0.1 on 2024-01-03 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='athlete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=30)),
                ('Second_name', models.CharField(max_length=30)),
                ('Country', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_score', models.BooleanField()),
                ('coaf_first', models.FloatField(default=0)),
                ('coaf_second', models.FloatField(default=0)),
            ],
        ),
    ]