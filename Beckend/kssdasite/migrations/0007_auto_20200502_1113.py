# Generated by Django 2.2.4 on 2020-05-02 05:13

from django.db import migrations, models
import kssdasite.models


class Migration(migrations.Migration):

    dependencies = [
        ('kssdasite', '0006_auto_20190823_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='picture',
            field=models.ImageField(blank=True, max_length=50, null=True, upload_to=kssdasite.models.upload_location),
        ),
    ]