# Generated by Django 3.1.7 on 2022-01-28 02:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_auto_20220127_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='contact_email',
            field=models.CharField(default='none', max_length=30),
        ),
        migrations.AddField(
            model_name='job',
            name='contact_phone',
            field=models.CharField(default='none', max_length=20),
        ),
        migrations.AddField(
            model_name='job',
            name='deadline',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='job',
            name='job_type',
            field=models.CharField(default='none', max_length=10),
        ),
        migrations.AddField(
            model_name='job',
            name='requirement',
            field=models.TextField(default='none'),
        ),
        migrations.AddField(
            model_name='job',
            name='responsibility',
            field=models.TextField(default='none'),
        ),
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(default='none', max_length=20),
        ),
    ]
