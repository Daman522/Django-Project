# Generated by Django 3.2.6 on 2021-08-30 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myappp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=None),
        ),
    ]