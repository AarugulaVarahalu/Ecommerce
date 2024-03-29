from django.db import models

# Create your models here.


class Catageory(models.Model):

    name = models.CharField(max_length=220, blank=False)

    def __str__(self):

        return self.name
    
class Products(models.Model):

    catageory = models.ForeignKey(Catageory, on_delete=models.SET_NULL, null=True, blank=True)
    product_name = models.CharField(max_length=225)
    img = models.ImageField(null=False, blank=False, upload_to='photos/')
    description = models.TextField()
    cost = models.IntegerField()
    is_active = models.BooleanField(default=False)


    def __str__(self):
        return self.product_name