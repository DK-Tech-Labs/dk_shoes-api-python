from django.db import models


class Product(models.Model):
    class Meta:
        ordering = ["id"]

    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    stock = models.IntegerField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    availability = models.BooleanField(default=True)

    # on delete deverar deletar apenas o product
    category = models.ForeignKey(
        "Categories", on_delete=models.CASCADE, related_name="products"
    )
   

class Assets(models.Model):
    class Meta:
        ordering = ["id"]

    url = models.TextField()
    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, related_name="assets"
    )


class Categories(models.Model):
    class Meta:
        ordering = ["id"]

    name = models.CharField(max_length=75)


class Sizes(models.Model):
    class Meta:
        ordering = ["id"]

    size_name = models.CharField(max_length=10)
    size_stock = models.IntegerField()
    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, related_name="sizes"
    )


class Colors(models.Model):
    class Meta:
        ordering = ["id"]

    color_name = models.CharField(max_length=10)
    color_stock = models.IntegerField()
    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, related_name="colors"
    )
