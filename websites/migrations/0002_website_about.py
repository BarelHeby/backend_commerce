# Generated by Django 4.1.9 on 2023-05-15 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='about',
            field=models.TextField(default=''),
        ),
    ]
