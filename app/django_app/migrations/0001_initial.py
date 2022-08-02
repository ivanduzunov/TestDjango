# Generated by Django 4.0.6 on 2022-08-01 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sport', models.TextField(max_length=100)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('birth_date', models.DateField(null=True)),
            ],
        ),
    ]