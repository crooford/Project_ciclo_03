# Generated by Django 4.1 on 2022-09-30 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0014_ordenmesas_orden'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordenmesa',
            name='platos',
        ),
        migrations.RemoveField(
            model_name='ordenmesas',
            name='orden',
        ),
    ]