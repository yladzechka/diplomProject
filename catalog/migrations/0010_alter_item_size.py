# Generated by Django 4.1.7 on 2023-03-13 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_alter_item_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='size',
            field=models.CharField(blank=True, choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], max_length=3, null=True),
        ),
    ]
