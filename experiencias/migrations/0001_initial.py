# Generated by Django 4.0.5 on 2022-06-23 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experiencias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=50)),
                ('fecha', models.DateTimeField(null=True)),
                ('autor', models.CharField(max_length=50)),
                ('cuerpo', models.CharField(max_length=10000)),
            ],
            options={
                'verbose_name': 'Experiencias',
                'verbose_name_plural': 'Experiencias',
            },
        ),
    ]
