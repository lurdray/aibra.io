# Generated by Django 4.1 on 2022-08-25 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0005_alter_appuser_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='charge',
            field=models.CharField(default='0', max_length=30, null=True),
        ),
    ]
