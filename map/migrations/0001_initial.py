# Generated by Django 3.0.4 on 2020-07-04 19:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.TextField(max_length=20)),
                ('lat', models.FloatField(default=0)),
                ('lang', models.FloatField(default=0)),
                ('ArabicName', models.TextField(max_length=100)),
                ('suspect', models.IntegerField(default=0)),
                ('confirme', models.IntegerField(default=0)),
                ('critique', models.IntegerField(default=0)),
                ('mort', models.IntegerField(default=0)),
                ('guerie', models.IntegerField(default=0)),
                ('degre', models.IntegerField(default=0)),
                ('date_validation', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='HistoriqueRegion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suspect', models.IntegerField(default=0)),
                ('confirme', models.IntegerField(default=0)),
                ('critique', models.IntegerField(default=0)),
                ('mort', models.IntegerField(default=0)),
                ('guerie', models.IntegerField(default=0)),
                ('degre', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('valide', models.BooleanField(default=False)),
                ('supprime', models.BooleanField(default=False)),
                ('vu', models.BooleanField(default=False)),
                ('agent', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('region', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='map.Region')),
            ],
        ),
        migrations.CreateModel(
            name='CentreReception',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.TextField(max_length=50)),
                ('numero', models.TextField(max_length=20)),
                ('adresse', models.TextField(max_length=20)),
                ('region', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='map.Region')),
            ],
        ),
    ]
