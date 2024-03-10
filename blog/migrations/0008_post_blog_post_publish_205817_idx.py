# Generated by Django 5.0.2 on 2024-03-10 08:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['published_date'], name='blog_post_publish_205817_idx'),
        ),
    ]