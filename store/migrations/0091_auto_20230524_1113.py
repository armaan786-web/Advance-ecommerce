# Generated by Django 3.2.18 on 2023-05-24 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0090_product_win_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='win_status',
        ),
        migrations.AddField(
            model_name='productbidders',
            name='win_status',
            field=models.CharField(choices=[('won', 'Won'), ('lost', 'Lost'), ('pending', 'pending')], default='pending', max_length=10),
        ),
    ]