# Generated by Django 4.1 on 2022-08-25 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0004_appuser_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='bio',
            field=models.TextField(default='This agency have not updated their bio..'),
        ),
    ]
