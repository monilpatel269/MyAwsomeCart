from django.db import models

# Create your models here.

class Blogpost(models.Model):
    post_id = models.AutoField(primary_key= True)
    title = models.CharField(max_length=50,default="")
    author = models.CharField(max_length=300,default="")
    content = models.TextField(default="")
    pub_date = models.DateField()
    thumbnail = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    contact_id = models.AutoField
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=30, default="")
    phone = models.IntegerField(default="")
    desc = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name