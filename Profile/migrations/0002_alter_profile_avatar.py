# Generated by Django 4.1.4 on 2023-01-02 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='img/default.jpg', upload_to='profile_images'),
        ),
    ]
