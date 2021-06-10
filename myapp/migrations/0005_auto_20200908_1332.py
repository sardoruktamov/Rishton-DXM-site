# Generated by Django 3.0.8 on 2020-09-08 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20200908_0846'),
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('berth', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=12)),
                ('address', models.CharField(max_length=300)),
            ],
        ),
        migrations.RemoveField(
            model_name='employee',
            name='edate',
        ),
    ]
