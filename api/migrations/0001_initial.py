# Generated by Django 4.0.6 on 2022-08-07 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('rating', models.IntegerField(default=0)),
                ('tier', models.CharField(blank=True, max_length=15)),
            ],
        ),
    ]
