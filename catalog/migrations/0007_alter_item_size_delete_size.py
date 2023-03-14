# Generated by Django 4.1.7 on 2023-03-13 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_item_discount_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='size',
            field=models.CharField(blank=True, choices=[('XS', 'eXtra Small'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'eXtra Large'), ('XXL', 'eXtra eXtra Large')], max_length=6, null=True),
        ),
        migrations.DeleteModel(
            name='Size',
        ),
    ]