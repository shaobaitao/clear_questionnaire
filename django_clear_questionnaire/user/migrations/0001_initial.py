# Generated by Django 3.1.6 on 2021-08-12 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='USER',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=60)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=60)),
                ('state', models.IntegerField()),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='USER_LOGIN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('login_time', models.DateTimeField(auto_now=True)),
                ('ip', models.GenericIPAddressField()),
                ('os', models.CharField(max_length=200)),
                ('login_mode', models.CharField(default='', max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='USER_INFO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_time', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('gender', models.IntegerField()),
                ('avatar', models.ImageField(upload_to='avatar')),
                ('nickname', models.CharField(max_length=100)),
                ('birthday', models.DateField(default='1900-01-01')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.user')),
            ],
        ),
    ]
