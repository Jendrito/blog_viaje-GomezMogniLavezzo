# Generated by Django 4.0.5 on 2022-06-21 20:12

from django.db import migrations, models
import multiprocessing.sharedctypes


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta', '0007_alter_user_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='imagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, default='usuario1.jpg', null=multiprocessing.sharedctypes.Value, upload_to='blog_viaje-GomezMogniLavezzo')),
            ],
        ),
    ]
