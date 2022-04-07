from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

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
    
class BlogComment(models.Model):
    sno= models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Blogpost, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    timestamp= models.DateTimeField(default=now)
    
    def __str__(self):
        return self.user.username

class Contact(models.Model):
    contact_id = models.AutoField
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=30, default="")
    phone = models.IntegerField(default="")
    desc = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name
