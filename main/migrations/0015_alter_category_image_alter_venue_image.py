# Generated by Django 4.1.7 on 2023-03-25 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_venue_lat_venue_lon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='category/', verbose_name='Рисунок'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='image',
            field=models.ImageField(upload_to='venue/', verbose_name='Рисунок'),
        ),
    ]
