# Generated by Django 4.0.5 on 2022-06-22 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta', '0018_alter_user_profile_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='imagen',
            field=models.ImageField(default='WhatsApp_Image_2022-06-21_at_3.27.06_PM.jpeg', upload_to='profile_image'),
        ),
    ]