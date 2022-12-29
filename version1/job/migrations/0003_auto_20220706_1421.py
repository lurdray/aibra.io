# Generated by Django 3.1.7 on 2022-07-06 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_jobresultconnector'),
        ('quiz', '0002_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobresultconnector',
            name='result',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.result'),
        ),
        migrations.AddField(
            model_name='job',
            name='results',
            field=models.ManyToManyField(through='job.JobResultConnector', to='quiz.Result'),
        ),
    ]