# Generated by Django 3.0.3 on 2020-03-10 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0002_cat_available'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cat',
            name='color',
        ),
    ]