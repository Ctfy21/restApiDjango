# Generated by Django 5.0.1 on 2024-02-01 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experimentAPI', '0003_alter_experiment_start_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='box',
            old_name='title',
            new_name='box_number',
        ),
    ]