# Generated by Django 2.2.4 on 2020-05-13 19:55

from django.db import migrations, models
import kssdasite.models


class Migration(migrations.Migration):

    dependencies = [
        ('kssdasite', '0008_auto_20200513_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='picture',
            field=models.ImageField(blank=True, max_length=50, null=True, upload_to=kssdasite.models.upload_location),
        ),
    ]
