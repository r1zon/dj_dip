from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    product_type = models.CharField(max_length=50, blank=True, null=True)
    img = models.FileField(upload_to='products/')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']

class Review(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    text = models.TextField()
    rate =  models.IntegerField(default=0, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product.name) + ' ' + self.text[:50]