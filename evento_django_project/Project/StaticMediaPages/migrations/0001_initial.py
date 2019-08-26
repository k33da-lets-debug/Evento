# Generated by Django 2.2.4 on 2019-08-25 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carosoul',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('contact_no', models.CharField(max_length=50)),
                ('message', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='CreateEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('contact_no', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('CORPORATE_EVENT', 'Corporate event'), ('WEDDING_PLANNER', 'Wedding planner'), ('SOCIAL_EVENT', 'Social event')], max_length=20)),
                ('company_name', models.CharField(blank=True, max_length=100)),
                ('date', models.DateTimeField()),
                ('event_description', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]