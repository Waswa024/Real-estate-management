# Generated by Django 4.2.4 on 2024-01-17 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('price', models.IntegerField()),
                ('num_of_bedrooms', models.IntegerField()),
                ('num_of_birthrooms', models.IntegerField()),
                ('square_footage', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
