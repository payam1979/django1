# Generated by Django 5.0.2 on 2024-03-14 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_alter_contact_subject'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['-created_date']},
        ),
    ]