# Generated by Django 4.0.5 on 2022-06-27 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tramites', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tramites',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes'),
        ),
        migrations.AddField(
            model_name='tramites',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
