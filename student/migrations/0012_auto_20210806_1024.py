# Generated by Django 3.0.2 on 2021-08-06 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0011_merge_20210802_2345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='additionaldetails',
            name='student_id',
        ),
        migrations.RemoveField(
            model_name='contactdetails',
            name='student_id',
        ),
        migrations.RemoveField(
            model_name='documents',
            name='student_id',
        ),
        migrations.RemoveField(
            model_name='parentdetails',
            name='student_id',
        ),
    ]
