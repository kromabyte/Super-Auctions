# Generated by Django 4.0.6 on 2022-08-23 04:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_watchlist_delete_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='bids',
            name='bidder',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]