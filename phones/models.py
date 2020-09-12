from django.db import models
from django.utils.text import slugify

from django.conf import settings

class Product(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    # product_type = models.CharField(max_length=50, default='phone')
    product_type = models.ForeignKey('ProductType', on_delete=models.CASCADE)
    img = models.ImageField(upload_to='products/')
    slug = models.SlugField(('slug'), unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']


class ProductType(models.Model):
    product_type = models.CharField(max_length=50, default='phone')

    def __str__(self):
        return self.product_type

class Review(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    text = models.TextField()
    rate = models.IntegerField(default=0, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product.name) + ' ' + self.text[:50]


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='ProductCounts', related_name='orders')
    is_ordered = models.BooleanField(default=False)

    def __str__(self):
        return f'Заказ №{self.pk}'


class ProductCounts(models.Model):
    product = models.ForeignKey('Product', related_name='product_counts', on_delete=models.CASCADE)
    order = models.ForeignKey('Order', related_name='product_counts', on_delete=models.CASCADE)
    count = models.IntegerField(default=1)
