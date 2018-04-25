# Generated by Django 2.0.4 on 2018-04-24 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordinality', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=24, unique=True)),
                ('size', models.FloatField(help_text='Units of Earth Masses')),
                ('distance', models.FloatField(help_text='Units of Astronomical Units')),
                ('description', models.TextField()),
            ],
        ),
    ]