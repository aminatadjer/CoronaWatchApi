# Generated by Django 3.0.4 on 2020-06-20 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supprime', models.BooleanField(default=False)),
                ('contenu', models.TextField()),
            ],
        ),
    ]