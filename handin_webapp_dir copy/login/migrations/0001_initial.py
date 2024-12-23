# Generated by Django 5.1.3 on 2024-12-23 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NotConfirmedUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.TextField(max_length=100)),
                ('username', models.CharField(max_length=50, unique='True')),
                ('email', models.EmailField(max_length=254)),
                ('department', models.CharField(max_length=60)),
                ('codigo', models.CharField(max_length=15)),
                ('password', models.TextField(max_length=150)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.TextField(max_length=100)),
                ('username', models.CharField(max_length=50, unique='True')),
                ('email', models.EmailField(max_length=254)),
                ('department', models.CharField(max_length=60)),
                ('codigo', models.CharField(max_length=15)),
                ('password', models.TextField(max_length=150)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
