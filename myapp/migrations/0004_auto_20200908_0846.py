# Generated by Django 3.0.8 on 2020-09-08 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20200905_2033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='eemail',
        ),
        migrations.AddField(
            model_name='employee',
            name='edate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='econtact',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
