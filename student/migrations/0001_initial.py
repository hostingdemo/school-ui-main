# Generated by Django 3.2.4 on 2021-06-10 13:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100, null=True)),
                ('lastname', models.CharField(max_length=100, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Male', max_length=100)),
                ('DOB', models.DateField(null=True)),
                ('admission_Number', models.CharField(max_length=12, null=True)),
                ('religion', models.CharField(blank=True, max_length=100, null=True)),
                ('caste', models.CharField(blank=True, max_length=100, null=True)),
                ('aadhar', models.CharField(max_length=12, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ParentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('father_name', models.CharField(max_length=100, null=True)),
                ('mother_name', models.CharField(max_length=100, null=True)),
                ('father_dob', models.DateField(blank=True, null=True)),
                ('mother_dob', models.DateField(blank=True, null=True)),
                ('phone_no', models.BigIntegerField()),
                ('alternate_phone_no', models.BigIntegerField()),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('father_quali', models.CharField(blank=True, max_length=100, null=True)),
                ('mother_quali', models.CharField(blank=True, max_length=100, null=True)),
                ('family_annual_income', models.IntegerField(default=0)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(default='shri.jpg', null=True, upload_to='media')),
                ('id_proof', models.FileField(blank=True, null=True, upload_to='media')),
                ('caste_certificate', models.FileField(blank=True, null=True, upload_to='media')),
                ('domicile', models.FileField(blank=True, null=True, upload_to='media')),
                ('transfer_certificate', models.FileField(blank=True, null=True, upload_to='media')),
                ('character_certificate', models.FileField(blank=True, null=True, upload_to='media')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ContactDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_addr', models.CharField(max_length=100, null=True)),
                ('current_addr2', models.CharField(max_length=100, null=True)),
                ('state', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('pincode', models.CharField(default='00000', max_length=10, null=True)),
                ('permanent_addr', models.CharField(blank=True, max_length=100, null=True)),
                ('permanent_addr2', models.CharField(blank=True, max_length=100, null=True)),
                ('permanent_state', models.CharField(blank=True, max_length=100, null=True)),
                ('permanent_city', models.CharField(blank=True, max_length=100, null=True)),
                ('permanent_pincode', models.CharField(default='00000', max_length=10, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AdditionalDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('privious_school', models.CharField(blank=True, max_length=100, null=True)),
                ('transfer_certificate_no', models.CharField(blank=True, max_length=100, null=True)),
                ('fee_waiver_category', models.CharField(blank=True, max_length=100, null=True)),
                ('route_code', models.CharField(blank=True, max_length=100, null=True)),
                ('shift', models.CharField(blank=True, max_length=100, null=True)),
                ('stoppage_name', models.CharField(blank=True, max_length=100, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
