# Generated by Django 3.2 on 2021-09-24 22:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0007_auto_20210924_2206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='followers',
        ),
        migrations.AddField(
            model_name='user',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='_network_user_followers_+', to=settings.AUTH_USER_MODEL),
        ),
    ]
