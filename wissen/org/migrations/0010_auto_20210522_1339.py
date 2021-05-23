# Generated by Django 3.2.3 on 2021-05-22 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('org', '0009_auto_20210320_0019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='id',
        ),
        migrations.RemoveField(
            model_name='subscriber',
            name='id',
        ),
        migrations.RemoveField(
            model_name='team',
            name='id',
        ),
        migrations.RemoveField(
            model_name='testimonial',
            name='id',
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(blank=True, max_length=30, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='email',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='team',
            name='email',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='email',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False),
        ),
    ]