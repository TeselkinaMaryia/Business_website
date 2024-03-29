# Generated by Django 4.1.7 on 2023-03-26 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_delete_directors'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cantact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
    ]
