# Generated by Django 3.0.4 on 2020-07-05 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='vu',
            field=models.BooleanField(default=False),
        ),
    ]