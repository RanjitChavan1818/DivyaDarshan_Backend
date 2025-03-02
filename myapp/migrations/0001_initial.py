# Generated by Django 5.1.6 on 2025-02-19 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DarshanUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('md1', models.CharField(help_text='Safety Field 1', max_length=255)),
                ('md2', models.CharField(help_text='Safety Field 2', max_length=255)),
                ('md3', models.CharField(help_text='Safety Field 3', max_length=255)),
                ('otp', models.CharField(blank=True, help_text='OTP for email verification', max_length=6, null=True)),
            ],
        ),
    ]
