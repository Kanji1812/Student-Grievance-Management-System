# Generated by Django 4.2.5 on 2024-04-09 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_alter_studentmaster_enrollment_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmaster',
            name='barcode',
            field=models.ImageField(blank=True, null=True, upload_to='StudentImg/'),
        ),
    ]