# Generated by Django 4.0.5 on 2022-06-30 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tramites', '0005_tramites_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tramites',
            name='descripcion',
            field=models.TextField(max_length=5000),
        ),
    ]
