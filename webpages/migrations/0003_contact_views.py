# Generated by Django 3.0.3 on 2020-12-06 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0002_contact_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]