# Generated by Django 2.2 on 2021-01-01 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0011_auto_20201231_0722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='emp_id',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
