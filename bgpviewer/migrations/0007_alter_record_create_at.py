# Generated by Django 4.2.1 on 2023-05-18 08:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bgpviewer', '0006_alter_record_create_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='create_at',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
    ]
