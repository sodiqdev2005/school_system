# Generated by Django 4.1.5 on 2023-02-15 10:43

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0003_remove_contest_end_time_remove_contest_start_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contest',
            name='url_contest',
        ),
        migrations.AlterField(
            model_name='contest',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
