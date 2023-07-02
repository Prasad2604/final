from django.db import models

# Create your models here.

class Cafe(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    price = models.IntegerField(default=0)
    pub_date = models.DateField()

    def __str__(self):
        return self.product_name



class Restaurant(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    price = models.IntegerField(default=0)
    pub_date = models.DateField()


    def __str__(self):
        return self.product_name