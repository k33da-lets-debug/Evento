# Generated by Django 2.2.4 on 2019-08-26 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StaticMediaPages', '0005_auto_20190825_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createevent',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]