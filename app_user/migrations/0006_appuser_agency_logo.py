# Generated by Django 3.1.7 on 2022-02-20 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0005_auto_20220220_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='agency_logo',
            field=models.CharField(default='', max_length=30),
        ),
    ]
