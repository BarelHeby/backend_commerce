# Generated by Django 4.1.9 on 2023-05-14 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('website_name', models.CharField(default=None, max_length=100)),
                ('adminPassword', models.CharField(default=None, max_length=50)),
            ],
        ),
    ]
