# Generated by Django 5.1.6 on 2025-02-26 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reniorsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
