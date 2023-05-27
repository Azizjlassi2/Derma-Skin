# Generated by Django 4.1.7 on 2023-05-27 13:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Accounts", "0005_rename_followers_appuser_contacted_users"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appuser",
            name="contacted_users",
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
