# Generated by Django 5.1.1 on 2024-09-15 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=150)),
                ('price', models.IntegerField()),
                ('release_date', models.CharField(max_length=15)),
                ('lte_exists', models.CharField(max_length=5)),
                ('slug', models.SlugField()),
            ],
        ),
    ]
