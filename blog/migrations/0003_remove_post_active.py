# Generated by Django 3.2.18 on 2023-04-25 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20230425_1429'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='active',
        ),
    ]