# Generated by Django 3.2.4 on 2021-06-24 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='text',
            name='emotion',
        ),
        migrations.DeleteModel(
            name='Emotion',
        ),
    ]
