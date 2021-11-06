# Generated by Django 3.2.7 on 2021-11-03 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weblog', '0002_remove_category_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='childeren', to='weblog.category', verbose_name='زیر  گروه'),
        ),
    ]