# Generated by Django 4.1 on 2022-08-30 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("libreria", "0002_alter_employee_second_lastname_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="employee", name="category",),
        migrations.RemoveField(model_name="employee", name="position",),
        migrations.RemoveField(model_name="employee", name="username",),
        migrations.RemoveField(model_name="menu", name="category",),
        migrations.DeleteModel(name="Category",),
        migrations.DeleteModel(name="Employee",),
        migrations.DeleteModel(name="Menu",),
        migrations.DeleteModel(name="Position",),
        migrations.DeleteModel(name="User",),
    ]
