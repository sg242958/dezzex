# Generated by Django 3.0.8 on 2020-07-22 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='user',
        ),
        migrations.AddField(
            model_name='registration',
            name='email',
            field=models.EmailField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='registration',
            name='full_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='registration',
            name='password',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='registration',
            name='repassword',
            field=models.CharField(default='', max_length=20),
        ),
    ]