# Generated by Django 3.0.5 on 2020-04-14 00:48

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_cmspages_upload'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('upload', models.ImageField(null=True, upload_to='uploads/')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('is_active', models.BooleanField()),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]