# Generated by Django 3.1.7 on 2022-07-06 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_auto_20220706_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='barrier',
            field=models.IntegerField(default=50),
        ),
    ]
