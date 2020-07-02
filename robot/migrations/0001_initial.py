# Generated by Django 3.0.4 on 2020-07-02 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Veille',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('type', models.CharField(choices=[('youtube', 'scrapped from youtube'), ('twitter', 'scrapped from twitter'), ('google', 'scrapped from google search feed')], default='youtube', max_length=50)),
                ('titre', models.TextField()),
                ('description', models.TextField()),
                ('date', models.CharField(default=None, max_length=40)),
                ('valide', models.BooleanField(default=False)),
                ('supprime', models.BooleanField(default=False)),
            ],
        ),
    ]
