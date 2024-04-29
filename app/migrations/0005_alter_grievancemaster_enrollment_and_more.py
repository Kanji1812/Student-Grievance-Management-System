# Generated by Django 5.0.2 on 2024-03-17 10:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_studentmaster_hod_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grievancemaster',
            name='Enrollment',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='studentmaster',
            name='enrollment_no',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
    ]
