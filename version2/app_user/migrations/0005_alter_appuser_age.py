# Generated by Django 4.1.3 on 2022-12-11 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0004_alter_appuser_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='age',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
