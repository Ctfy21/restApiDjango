# Generated by Django 5.0.1 on 2024-02-01 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experimentAPI', '0004_rename_title_box_box_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variety',
            name='relative_template_percent',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='variety',
            name='score',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='variety',
            name='sequence_number',
            field=models.IntegerField(default=0),
        ),
    ]
