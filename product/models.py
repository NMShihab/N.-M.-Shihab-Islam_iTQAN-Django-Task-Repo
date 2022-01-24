from django.db import models
from django.contrib.auth.models import  User

# Create your models here.
class BaseClass(models.Model):
    title = models.CharField(max_length = 255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        ordering = ['title']


class Categories(BaseClass):
    image = models.ImageField(upload_to='categories')
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "http://127.0.0.1:8000/media/"+str(self.image)


class Product(BaseClass):
    category = models.ForeignKey(Categories, on_delete= models.CASCADE)
    image = models.ImageField(upload_to='product')
    
    class Meta(BaseClass.Meta):
        ordering = ['-created']
    
    def __str__(self):
        return self.title

    


class Views(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created']
    
    def __str__(self):
        return str(self.product)
    
        
    
    