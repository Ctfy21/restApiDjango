# Generated by Django 5.0.1 on 2024-02-01 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experimentAPI', '0009_rename_box_currentvalues_box_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='currentvalues',
            old_name='box_id',
            new_name='referring_box',
        ),
        migrations.RenameField(
            model_name='currentvalues',
            old_name='experiment_id',
            new_name='referring_experiment',
        ),
        migrations.RenameField(
            model_name='currentvalues',
            old_name='variety_id',
            new_name='referring_variety',
        ),
    ]
