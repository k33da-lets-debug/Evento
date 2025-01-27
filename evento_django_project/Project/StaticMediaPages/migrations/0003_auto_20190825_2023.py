# Generated by Django 2.2.4 on 2019-08-25 14:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('StaticMediaPages', '0002_auto_20190825_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='image',
            field=models.ImageField(default='1.0', upload_to='gallery/'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='publish',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='gallery',
            name='publish_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
