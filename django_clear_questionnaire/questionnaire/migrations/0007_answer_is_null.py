# Generated by Django 3.1.6 on 2022-01-12 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0006_question_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='is_null',
            field=models.BooleanField(default=0),
        ),
    ]
