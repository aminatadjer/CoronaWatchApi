# Generated by Django 3.0.4 on 2020-06-01 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
        ('coronawatch', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informationsvirus',
            name='region',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='map.Region'),
        ),
    ]