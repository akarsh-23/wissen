# Generated by Django 3.2.3 on 2021-05-23 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('org', '0013_auto_20210522_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
