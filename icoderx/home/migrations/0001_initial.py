# Generated by Django 3.0.14 on 2021-11-30 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('content', models.TextField()),
            ],
        ),
    ]