from email.policy import default
from pyexpat import model
from statistics import mode
from unicodedata import category
from django.db import models
from django.forms import modelformset_factory
from numpy import product

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50,default="")
    desc = models.CharField(max_length=300)
    price = models.IntegerField(default=0)
    pub_date = models.DateField()
    img = models.ImageField(upload_to="shop/images", default="")
    
    def __str__(self):
        return self.product_name

class Contact(models.Model):
    contact_id = models.AutoField
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=30, default="")
    phone = models.IntegerField(default="")
    desc = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name
    
class Orders(models.Model):
   order_id= models.AutoField(primary_key=True)
   items_json = models.CharField(max_length=5000)
   name=models.CharField(max_length=90)
   email=models.CharField(max_length=111)
   address=models.CharField(max_length=111)
   city=models.CharField(max_length=111)
   state=models.CharField(max_length=111)
   zip_code=models.CharField(max_length=111)
   phone=models.CharField(max_length=10,default="")
   class Meta:
        verbose_name_plural="Orders"
   
   def __str__(self):
        return self.name
    
class OrderUpdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."