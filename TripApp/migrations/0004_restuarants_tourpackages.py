# Generated by Django 5.0.4 on 2024-05-07 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TripApp', '0003_hotels_hprice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restuarants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images')),
                ('location', models.TextField()),
                ('rating', models.FloatField()),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tourpackages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(verbose_name=100)),
                ('image', models.ImageField(upload_to='images')),
                ('location', models.TextField()),
                ('desc', models.TextField()),
                ('price', models.FloatField()),
            ],
        ),
    ]
