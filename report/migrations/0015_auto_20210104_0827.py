# Generated by Django 2.2 on 2021-01-04 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0014_auto_20210101_0536'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='comments',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='hours',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]