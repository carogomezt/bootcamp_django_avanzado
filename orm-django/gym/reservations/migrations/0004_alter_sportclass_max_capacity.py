# Generated by Django 5.1.7 on 2025-04-01 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0003_auto_20250401_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sportclass',
            name='max_capacity',
            field=models.PositiveIntegerField(default=10),
        ),
    ]
