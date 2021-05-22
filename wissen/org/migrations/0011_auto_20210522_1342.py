# Generated by Django 3.2.3 on 2021-05-22 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('org', '0010_auto_20210522_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
