# Generated by Django 4.1.5 on 2023-01-24 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_post', '0011_rename_author_like_liked_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='user',
        ),
    ]
