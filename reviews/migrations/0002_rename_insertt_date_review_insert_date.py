# Generated by Django 4.1.9 on 2023-05-15 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='insertt_date',
            new_name='insert_date',
        ),
    ]
