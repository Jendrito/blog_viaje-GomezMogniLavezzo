# Generated by Django 4.0.5 on 2022-06-28 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta', '0004_alter_user_redes_sociales'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes_User/'),
        ),
    ]
