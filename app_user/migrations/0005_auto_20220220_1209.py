# Generated by Django 3.1.7 on 2022-02-20 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0004_auto_20220220_0245'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='agency_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='facebook_link',
            field=models.CharField(default='#', max_length=10),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='github_link',
            field=models.CharField(default='#', max_length=10),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='instagram_link',
            field=models.CharField(default='#', max_length=10),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='twitter_link',
            field=models.CharField(default='#', max_length=10),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='whatsapp_link',
            field=models.CharField(default='#', max_length=10),
        ),
    ]
