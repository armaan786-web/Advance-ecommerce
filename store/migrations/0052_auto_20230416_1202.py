# Generated by Django 3.2.18 on 2023-04-16 19:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0051_auto_20230416_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productfaq',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='productfaq',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
