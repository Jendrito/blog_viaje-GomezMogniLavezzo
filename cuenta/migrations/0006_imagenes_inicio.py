# Generated by Django 4.0.5 on 2022-06-29 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta', '0005_user_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagenes_Inicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen1', models.ImageField(blank=True, null=True, upload_to='imagenes_Inicio/')),
                ('imagen2', models.ImageField(blank=True, null=True, upload_to='imagenes_Inicio/')),
                ('imagen3', models.ImageField(blank=True, null=True, upload_to='imagenes_Inicio/')),
            ],
        ),
    ]
