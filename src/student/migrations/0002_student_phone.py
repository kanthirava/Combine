# Generated by Django 2.0.7 on 2019-06-27 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='phone',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
