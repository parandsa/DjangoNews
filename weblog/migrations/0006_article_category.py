# Generated by Django 3.2.7 on 2021-10-28 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weblog', '0005_auto_20211028_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(to='weblog.Category'),
        ),
    ]