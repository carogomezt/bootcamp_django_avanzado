# Generated by Django 5.1.7 on 2025-04-01 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sportclass',
            name='max_capacity',
            field=models.PositiveIntegerField(default=20),
        ),
    ]
