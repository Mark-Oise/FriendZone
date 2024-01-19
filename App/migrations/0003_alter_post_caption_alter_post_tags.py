# Generated by Django 5.0 on 2024-01-12 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_profile_follower_list_profile_is_celebrity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.CharField(blank=True, max_length=10000, null=True, verbose_name='Caption'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='tags', to='App.tag'),
        ),
    ]
