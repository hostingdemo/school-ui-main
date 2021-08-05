# Generated by Django 3.0.2 on 2021-07-30 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_auto_20210730_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='additionaldetails',
            name='student_id',
            field=models.CharField(default='dfdfdfd', max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactdetails',
            name='student_id',
            field=models.CharField(default='dfdfdfd', max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='documents',
            name='student_id',
            field=models.CharField(default='dfdfdfdf', max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parentdetails',
            name='student_id',
            field=models.CharField(default='dfdfdfd', max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='student_id',
            field=models.CharField(default='dfdfdfd', max_length=100, unique=True),
            preserve_default=False,
        ),
    ]