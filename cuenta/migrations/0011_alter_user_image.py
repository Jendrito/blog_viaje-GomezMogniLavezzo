# Generated by Django 4.0.5 on 2022-06-30 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta', '0010_delete_imagenes_inicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='usuario.jpg', upload_to='imagenes_User/'),
        ),
    ]
