# Generated by Django 4.2.11 on 2025-07-23 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_account_email_alter_account_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='account',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='account',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('doctor', 'Doctor'), ('nurse', 'Nurse'), ('patient', 'Patient')], default='patient', max_length=20),
        ),
    ]
