# Generated by Django 2.2.2 on 2019-06-21 03:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('usercaption', '0004_remove_imagecaption_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagecaption',
            name='caption',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='imagecaption',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
