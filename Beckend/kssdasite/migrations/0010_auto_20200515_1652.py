# Generated by Django 2.2.4 on 2020-05-15 10:52

from django.db import migrations, models
import kssdasite.models


class Migration(migrations.Migration):

    dependencies = [
        ('kssdasite', '0009_auto_20200514_0155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=kssdasite.models.upload_location),
        ),
    ]