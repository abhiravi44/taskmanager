# Generated by Django 2.2 on 2021-01-06 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0024_auto_20210105_1159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='designation',
        ),
        migrations.RemoveField(
            model_name='team',
            name='user',
        ),
        migrations.AddField(
            model_name='profile',
            name='designation',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='report.Team'),
        ),
        migrations.AddField(
            model_name='team',
            name='members',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='report.Team'),
        ),
        migrations.AlterField(
            model_name='task',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='report.Team'),
        ),
        migrations.DeleteModel(
            name='Department',
        ),
    ]
