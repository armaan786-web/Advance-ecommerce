# Generated by Django 3.2.18 on 2023-04-25 02:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0064_product_hot_deal'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cartorderitem',
            options={'ordering': ['-date'], 'verbose_name_plural': '6. Cart Order Item'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-date'], 'verbose_name_plural': '1. Products'},
        ),
        migrations.AlterModelOptions(
            name='productbidders',
            options={'ordering': ['-date'], 'verbose_name_plural': '9 Product Bidders'},
        ),
        migrations.AlterModelOptions(
            name='productfaq',
            options={'ordering': ['-date'], 'verbose_name_plural': '7. Product Faqs'},
        ),
        migrations.AlterModelOptions(
            name='productoffers',
            options={'ordering': ['-date'], 'verbose_name_plural': 'Product Offers'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-date'], 'verbose_name_plural': '8. Reviews/Rating'},
        ),
    ]