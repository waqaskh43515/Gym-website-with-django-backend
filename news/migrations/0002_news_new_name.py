# Generated by Django 5.1.2 on 2024-10-23 19:55

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='new_name',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='Name', unique=True),
        ),
    ]