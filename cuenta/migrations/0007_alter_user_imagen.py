# Generated by Django 4.0.5 on 2022-06-21 20:03

from django.db import migrations, models
import multiprocessing.sharedctypes


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta', '0006_alter_user_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='imagen',
            field=models.ImageField(blank=True, default='usuario1.jpg', null=multiprocessing.sharedctypes.Value, upload_to='blog_viaje-GomezMogniLavezzo'),
        ),
    ]