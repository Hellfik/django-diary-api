# Generated by Django 3.2.4 on 2021-06-28 08:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20210624_1344'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='text',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AlterField(
            model_name='text',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
