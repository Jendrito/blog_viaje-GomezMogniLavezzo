# Generated by Django 3.0.7 on 2022-06-07 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiencias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiencias',
            name='fecha',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='experiencias',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
