# Generated by Django 4.2.1 on 2023-05-18 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bgpviewer', '0007_alter_record_create_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='create_at',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
