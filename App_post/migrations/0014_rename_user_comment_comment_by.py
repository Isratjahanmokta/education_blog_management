# Generated by Django 4.1.5 on 2023-01-24 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_post', '0013_comment_updated'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='comment_by',
        ),
    ]
