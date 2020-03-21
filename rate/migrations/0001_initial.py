# Generated by Django 3.0.4 on 2020-03-20 16:53

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('semester', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Taught_by_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('rate', models.IntegerField()),
                ('data_publish', models.DateTimeField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('professor_id', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Taught_by',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rate.Module')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rate.Teacher')),
            ],
        ),
    ]