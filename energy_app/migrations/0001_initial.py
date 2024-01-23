# Generated by Django 5.0.1 on 2024-01-22 21:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meter_name', models.CharField(max_length=32)),
                ('phases', models.IntegerField(default=1)),
                ('kt', models.IntegerField(default=1)),
                ('commercial', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('username', models.CharField(max_length=32)),
                ('region', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read_time', models.DateTimeField()),
                ('value', models.FloatField()),
                ('meter_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='energy_app.meter')),
            ],
        ),
        migrations.AddField(
            model_name='meter',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='energy_app.user'),
        ),
    ]
