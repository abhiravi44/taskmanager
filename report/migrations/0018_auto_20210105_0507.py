# Generated by Django 2.2 on 2021-01-05 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0017_auto_20210105_0505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='report.Department'),
        ),
    ]