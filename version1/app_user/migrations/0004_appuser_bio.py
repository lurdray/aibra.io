# Generated by Django 4.1 on 2022-08-25 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0003_alter_appuser_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='bio',
            field=models.TextField(default=' '),
        ),
    ]
