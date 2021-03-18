# Generated by Django 3.1.7 on 2021-03-13 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('org', '0002_subscriber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('document', models.FileField(upload_to='Team/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
