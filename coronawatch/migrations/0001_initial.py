# Generated by Django 3.0.4 on 2020-05-15 17:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valide', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='RebotSource',
            fields=[
                ('contenu', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='coronawatch.Publication')),
                ('source', models.TextField(max_length=20)),
                ('lien', models.URLField()),
            ],
            bases=('coronawatch.publication',),
        ),
        migrations.CreateModel(
            name='VideoInternaut',
            fields=[
                ('contenu', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='coronawatch.Publication')),
                ('titre', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('video', models.FileField(upload_to='')),
            ],
            bases=('coronawatch.publication',),
        ),
        migrations.CreateModel(
            name='EtatSante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poids', models.FloatField()),
                ('temperature', models.FloatField()),
                ('rythmeCardiaque', models.FloatField()),
                ('suspect', models.BooleanField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('publication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coronawatch.Publication')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['comment_date'],
            },
        ),
        migrations.CreateModel(
            name='InformationsVirus',
            fields=[
                ('contenu', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='coronawatch.Publication')),
                ('region', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='report.Region')),
            ],
            bases=('coronawatch.publication',),
        ),
    ]
