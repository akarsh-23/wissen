# Generated by Django 3.2.3 on 2021-05-22 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0002_rename_event_events'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Events',
            new_name='Event',
        ),
        migrations.RenameModel(
            old_name='Registrations',
            new_name='Registration',
        ),
    ]
