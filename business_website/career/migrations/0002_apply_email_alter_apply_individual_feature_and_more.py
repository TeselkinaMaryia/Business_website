# Generated by Django 4.1.7 on 2023-03-24 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='apply',
            name='individual_feature',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='apply',
            name='online_work',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='apply',
            name='work_in_the_office',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
