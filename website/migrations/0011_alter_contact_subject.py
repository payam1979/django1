# Generated by Django 5.0.2 on 2024-03-14 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_alter_contact_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.TextField(blank=True, null=True),
        ),
    ]
