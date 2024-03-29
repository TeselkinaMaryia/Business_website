# Generated by Django 4.1.7 on 2023-03-12 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('image', models.FileField(upload_to='news/')),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]
