# Generated by Django 4.2.1 on 2023-05-18 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bgpviewer', '0014_alter_record_prefix_alter_record_site_relist_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='relist',
            old_name='prefix',
            new_name='prefix_le',
        ),
        migrations.AlterField(
            model_name='prefix',
            name='prefix_le',
            field=models.CharField(max_length=50),
        ),
    ]
