# Generated by Django 3.0.5 on 2020-04-14 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_newsevent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsevent',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
