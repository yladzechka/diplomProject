# Generated by Django 4.1.7 on 2023-03-21 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0016_product_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='placeholder.png', upload_to='source/clothing_images/'),
        ),
    ]
