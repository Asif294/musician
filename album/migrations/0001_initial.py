# Generated by Django 5.0.6 on 2024-06-20 15:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('musicianAp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=255)),
                ('release_date', models.DateField()),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('musician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='musicianAp.musician')),
            ],
        ),
    ]
