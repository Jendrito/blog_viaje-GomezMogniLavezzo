# Generated by Django 4.0.5 on 2022-06-27 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiencias', '0004_alter_experiencias_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiencias',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes_experiencias'),
        ),
    ]
