# Generated by Django 3.0.4 on 2020-03-21 03:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0002_auto_20200321_1114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rate',
            name='user_id',
        ),
    ]
