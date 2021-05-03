# Generated by Django 2.2 on 2020-12-31 07:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0010_auto_20201231_0457'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='emp_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='image',
        ),
        migrations.AddField(
            model_name='project',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='report.Team'),
        ),
        migrations.AlterField(
            model_name='team',
            name='team',
            field=models.CharField(default='Software Development', max_length=50),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.CharField(blank=True, max_length=20)),
                ('image', models.FileField(blank=True, upload_to='media/')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
