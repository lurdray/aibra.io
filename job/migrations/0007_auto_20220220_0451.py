# Generated by Django 3.1.7 on 2022-02-20 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_auto_20220218_0951'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='address',
            field=models.TextField(default='none'),
        ),
        migrations.AddField(
            model_name='job',
            name='category',
            field=models.CharField(default='none', max_length=30),
        ),
        migrations.AddField(
            model_name='job',
            name='country',
            field=models.CharField(default='none', max_length=30),
        ),
    ]
