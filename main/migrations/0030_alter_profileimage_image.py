# Generated by Django 4.1.7 on 2023-03-25 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_alter_profileimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileimage',
            name='image',
            field=models.ImageField(default='https://экологиякрыма.рф/img/19893719.jpg', upload_to='profile/', verbose_name='Рисунок'),
        ),
    ]