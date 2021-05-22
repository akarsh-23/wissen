# Generated by Django 3.2.3 on 2021-05-22 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('status', models.BooleanField()),
                ('image', models.FileField(upload_to='Events/')),
            ],
        ),
        migrations.CreateModel(
            name='Registrations',
            fields=[
                ('event', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('phone', models.BigIntegerField()),
                ('registrationNo', models.BigIntegerField(blank=True)),
                ('college', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=50)),
            ],
        ),
    ]
