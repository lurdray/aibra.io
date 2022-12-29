# Generated by Django 4.1.3 on 2022-12-04 11:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_rename_detail_education_course_education_institution_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='KeySkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_one', models.CharField(blank=True, max_length=100, null=True)),
                ('skill_two', models.CharField(blank=True, max_length=100, null=True)),
                ('skill_three', models.CharField(blank=True, max_length=100, null=True)),
                ('skill_four', models.CharField(blank=True, max_length=100, null=True)),
                ('skill_five', models.CharField(blank=True, max_length=100, null=True)),
                ('skill_six', models.CharField(blank=True, max_length=100, null=True)),
                ('skill_seven', models.CharField(blank=True, max_length=100, null=True)),
                ('skill_eight', models.CharField(blank=True, max_length=100, null=True)),
                ('skill_nine', models.CharField(blank=True, max_length=100, null=True)),
                ('skill_ten', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.BooleanField(default=False)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
