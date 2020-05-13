# Generated by Django 2.1.15 on 2020-05-13 19:36

from django.db import migrations, models
import kssdasite.models


class Migration(migrations.Migration):

    dependencies = [
        ('kssdasite', '0007_auto_20200502_1113'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_names', models.CharField(max_length=100, verbose_name='Ad names')),
                ('company_name', models.CharField(max_length=100, verbose_name='Company name')),
                ('description', models.TextField(max_length=2000, verbose_name='Description')),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='picture',
            field=models.ImageField(blank=True, max_length=50, null=True, upload_to=kssdasite.models.upload_location),
        ),
    ]
