from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# class Size(models.Model):
#     name = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.name


class Item(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, blank=True, null=True)
    size = models.CharField(max_length=3, choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], blank=True, null=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount_price = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='clothing_images/', blank=True, default="clothing_placeholder.jpg")

    def __str__(self):
        return self.name

    def get_thing(self):
        return reverse('catalog-thing', args=[self.id])
