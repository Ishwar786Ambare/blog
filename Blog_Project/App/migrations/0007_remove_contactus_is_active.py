# Generated by Django 3.0.5 on 2020-04-14 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_contactus_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactus',
            name='is_active',
        ),
    ]
