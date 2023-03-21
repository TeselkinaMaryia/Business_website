from django.db import models


class Laptops(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default=None)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    screen_size = models.CharField(max_length=50)
    color = models.CharField(max_length=30)
    hard_disk_size = models.CharField(max_length=30)
    cpu_model = models.CharField(max_length=30)
    ram_memory_installed_size = models.CharField(max_length=30)
    operation_system = models.CharField(max_length=30)
    graphics_card_description = models.CharField(max_length=30)
    image_1 = models.FileField(upload_to='laptops')
    image_2 = models.FileField(upload_to='laptops')
    image_3 = models.FileField(upload_to='laptops')
    about = models.TextField()
    price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=20, default=None)

    def __str__(self):
        return self.name
