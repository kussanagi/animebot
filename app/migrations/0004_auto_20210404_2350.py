# Generated by Django 3.1.7 on 2021-04-04 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_title_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='episodes',
            field=models.CharField(blank=True, default='', max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='title',
            name='release_date',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]
