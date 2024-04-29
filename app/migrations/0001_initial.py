# Generated by Django 5.0.2 on 2024-03-03 09:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminMaster',
            fields=[
                ('id', models.CharField(editable=False, max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('email_id', models.EmailField(max_length=254, unique=True)),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'AdminMaster',
            },
        ),
        migrations.CreateModel(
            name='CollegeMaster',
            fields=[
                ('college_id', models.CharField(editable=False, max_length=32, primary_key=True, serialize=False)),
                ('college_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('address_of_college', models.TextField(blank=True, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'CollegeMaster',
            },
        ),
        migrations.CreateModel(
            name='TrustMaster',
            fields=[
                ('trust_id', models.CharField(editable=False, max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('gov_reg_id', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'TrustMaster',
            },
        ),
        migrations.CreateModel(
            name='DepartmentMaster',
            fields=[
                ('department_id', models.CharField(editable=False, max_length=32, primary_key=True, serialize=False)),
                ('dept_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('college', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.collegemaster')),
            ],
            options={
                'db_table': 'DepartmentMaster',
            },
        ),
        migrations.CreateModel(
            name='DirectorMaster',
            fields=[
                ('director_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=255)),
                ('img', models.ImageField(blank=True, null=True, upload_to='director_images/')),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.departmentmaster')),
            ],
            options={
                'db_table': 'DirectorMaster',
            },
        ),
        migrations.CreateModel(
            name='HODMaster',
            fields=[
                ('hod_id', models.CharField(editable=False, max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='hod_images/')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('director', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.directormaster')),
            ],
            options={
                'db_table': 'HODMaster',
            },
        ),
        migrations.CreateModel(
            name='UniversityMaster',
            fields=[
                ('university_id', models.AutoField(primary_key=True, serialize=False)),
                ('university_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='university_logos/')),
                ('password', models.CharField(max_length=255)),
                ('university_code', models.CharField(max_length=255, unique=True)),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('trust', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.trustmaster')),
            ],
            options={
                'db_table': 'UniversityMaster',
            },
        ),
        migrations.AddField(
            model_name='collegemaster',
            name='university_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.universitymaster'),
        ),
    ]