# Generated by Django 4.0.6 on 2022-08-16 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_rename_status_listing_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='active',
            new_name='status',
        ),
    ]
