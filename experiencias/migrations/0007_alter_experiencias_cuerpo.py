# Generated by Django 4.0.5 on 2022-06-30 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiencias', '0006_alter_experiencias_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiencias',
            name='cuerpo',
            field=models.TextField(max_length=10000),
        ),
    ]