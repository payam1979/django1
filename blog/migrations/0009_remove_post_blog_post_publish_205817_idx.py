# Generated by Django 5.0.2 on 2024-03-10 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_blog_post_publish_205817_idx'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='post',
            name='blog_post_publish_205817_idx',
        ),
    ]
