# Generated by Django 4.0.4 on 2022-05-22 02:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0016_alter_post_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comments_number',
        ),
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
    ]