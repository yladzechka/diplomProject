# Generated by Django 4.1.7 on 2023-03-17 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_rename_item_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='product_placeholder.jpg', upload_to='clothing_images/'),
        ),
    ]
