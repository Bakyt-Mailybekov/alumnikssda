# Generated by Django 2.2.4 on 2019-08-22 06:35

from django.db import migrations, models
import kssdasite.models


class Migration(migrations.Migration):

    dependencies = [
        ('kssdasite', '0002_auto_20190822_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='picture',
            field=models.ImageField(blank=True, max_length=50, null=True, upload_to=kssdasite.models.upload_location),
        ),
    ]
