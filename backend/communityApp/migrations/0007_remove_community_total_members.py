# Generated by Django 5.1.6 on 2025-02-25 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('communityApp', '0006_remove_community_members_community_total_members'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='community',
            name='total_members',
        ),
    ]
