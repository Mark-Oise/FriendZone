# Generated by Django 5.0 on 2024-01-17 10:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0010_remove_profile_follower_list_profile_following_list'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='following_list',
            field=models.ManyToManyField(blank=True, related_name='followed_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
