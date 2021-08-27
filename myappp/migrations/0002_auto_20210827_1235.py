# Generated by Django 3.2.6 on 2021-08-27 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myappp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=6000)),
                ('phone', models.IntegerField()),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female')], default='', max_length=25)),
            ],
        ),
        migrations.AlterField(
            model_name='phone',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phone', to='myappp.brand'),
        ),
    ]