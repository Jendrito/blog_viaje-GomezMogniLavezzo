# Generated by Django 4.0.5 on 2022-06-21 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta', '0003_alter_user_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='imagen',
            field=models.ImageField(upload_to='blog_viaje-GomezMogniLavezzo'),
        ),
    ]