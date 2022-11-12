from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripcion")
    # color

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripcion")
    barcode = models.IntegerField(verbose_name="Codigo de barras", blank=True)
    category = models.ManyToManyField(ProductCategory, verbose_name="Categorias")
    stock = models.IntegerField(verbose_name="Cantidad")
    price = models.FloatField(verbose_name="Precio")
    images = models.ImageField(upload_to="products/", verbose_name="Imagen")
