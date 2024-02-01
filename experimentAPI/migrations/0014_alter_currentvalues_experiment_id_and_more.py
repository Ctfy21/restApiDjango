# Generated by Django 5.0.1 on 2024-02-01 21:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experimentAPI', '0013_alter_currentvalues_box_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currentvalues',
            name='experiment_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='experiment', to='experimentAPI.experiment'),
        ),
        migrations.AlterField(
            model_name='currentvalues',
            name='variety_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='variety', to='experimentAPI.variety'),
        ),
    ]