# Generated by Django 5.0.2 on 2024-03-09 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['created_date']},
        ),
    ]
