# Generated by Django 5.0.1 on 2024-02-01 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experimentAPI', '0002_remove_currentvalues_regime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment',
            name='start_time',
            field=models.DateField(),
        ),
    ]
