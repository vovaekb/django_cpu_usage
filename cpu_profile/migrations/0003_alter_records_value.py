# Generated by Django 3.2.11 on 2022-01-12 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpu_profile', '0002_rename_record_records'),
    ]

    operations = [
        migrations.AlterField(
            model_name='records',
            name='value',
            field=models.FloatField(),
        ),
    ]
