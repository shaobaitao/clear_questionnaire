# Generated by Django 3.1.6 on 2021-09-03 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0005_question_serial_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='state',
            field=models.IntegerField(default=1),
        ),
    ]
