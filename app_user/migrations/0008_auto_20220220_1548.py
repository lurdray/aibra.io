# Generated by Django 3.1.7 on 2022-02-20 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0007_auto_20220220_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='agency_name',
            field=models.CharField(default='', max_length=30, null=True),
        ),
    ]
