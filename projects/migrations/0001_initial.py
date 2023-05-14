# Generated by Django 4.1.9 on 2023-05-14 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('websites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=250)),
                ('insert_date', models.DateTimeField()),
                ('is_in_use', models.BooleanField(default=False)),
                ('website', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='websites.website')),
            ],
        ),
    ]
