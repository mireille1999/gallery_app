# Generated by Django 3.2 on 2021-04-14 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myGalleryApp', '0004_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='img_location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myGalleryApp.location'),
        ),
    ]
