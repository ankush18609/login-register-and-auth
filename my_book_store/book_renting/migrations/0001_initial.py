# Generated by Django 4.2 on 2023-04-13 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=30)),
                ('renting_date', models.DateField()),
                ('returning_date', models.DateField()),
                ('instance', models.IntegerField(default=0)),
            ],
        ),
    ]
