# Generated by Django 3.1.7 on 2022-07-06 17:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_quiz_question_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='end',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='question_no',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='start',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]