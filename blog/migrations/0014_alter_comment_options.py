# Generated by Django 5.0.2 on 2024-03-17 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_rename_contact_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_date']},
        ),
    ]