# Generated by Django 3.1.6 on 2022-01-13 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0008_q_choice_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='a_completion',
            name='completion',
            field=models.ForeignKey(default=13, on_delete=django.db.models.deletion.DO_NOTHING, to='questionnaire.q_completion'),
            preserve_default=False,
        ),
    ]