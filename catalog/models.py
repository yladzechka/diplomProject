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


class Size(models.Model):
    name = models.CharField(max_length=3, choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Unisex'),
    )
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, blank=True, null=True)
    size = models.ManyToManyField(Size)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=0)
    quantity = models.DecimalField(default=1, max_digits=6, decimal_places=0)
    discount_price = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='clothing_images/', blank=True, default="placeholder.png")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='U')

    def __str__(self):
        return self.name

    def get_product(self):
        return reverse('catalog-item', args=[self.id])

    def add_to_cart(self):
        return reverse('cart-add', args=[self.id])
