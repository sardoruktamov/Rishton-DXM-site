# Generated by Django 3.0.8 on 2021-01-03 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_galereya_sana'),
    ]

    operations = [
        migrations.AddField(
            model_name='biz',
            name='sana',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='biz',
            name='vaqt',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='galereya',
            name='vaqt',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
    ]
