# Generated by Django 4.0.1 on 2022-01-29 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='flower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Class', models.TextField()),
                ('Sepal_length', models.FloatField()),
                ('Sepal_width', models.FloatField()),
                ('Petal_length', models.FloatField()),
                ('Petal_width', models.FloatField()),
            ],
        ),
    ]
