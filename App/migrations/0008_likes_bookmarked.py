# Generated by Django 5.0 on 2024-01-15 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_post_likes_list_alter_profile_follower_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='likes',
            name='bookmarked',
            field=models.BooleanField(default=False),
        ),
    ]
