# Generated by Django 3.2.7 on 2021-11-03 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weblog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
    ]
