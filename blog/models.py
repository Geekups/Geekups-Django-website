from django.db import models
from django.contrib.auth.models import User 




# ----------------------------Article model --------------------

class Category(models.Model):
    name   = models.CharField(max_length=100)
    def __str__(self): 
        return self.name

class Article(models.Model):
    title   = models.CharField(max_length=100)
    content = models.TextField()
    publish = models.BooleanField(default=True)
    image   = models.ImageField(upload_to='images/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    #category   = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE,)
    likes = models.PositiveIntegerField(default=0)
    rating = models.FloatField(default=0.0)  # Assuming average rating

    #total_like = 
    #avr_rating = 

    def __str__(self):
        return self.title
    


class Comment(models.Model):
    
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publish = models.BooleanField(default=True)
    #total_like =
    #total_dislike =
    
    def __str__(self):
        return self.text





#-------------------Product -------------------------------
class ProductCategory(models.Model):
     
     name = models.CharField(max_length=100)
     
     def __str__(self):
        return self.name
    

class Product(models.Model):
    
     title   = models.CharField(max_length=100)
     content = models.TextField()
     image   = models.ImageField(upload_to='images/', blank=True)
     category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
     
     def __str__(self):
        return self.title
        

#----------------------end----------------------------------

#----------------------member-------------------------------

class Member(models.Model):
    f_name   = models.CharField(max_length=50)
    l_name   = models.CharField(max_length=50)
    image   = models.ImageField(upload_to='images/', blank=True)
    bio  = models.TextField()
    #email = models.EmailField(max_length=254)
    #publish = models.BooleanField(default=True)



#----------------------end--------------------------------

class Contact(models.Model):
    email = models.EmailField(max_length=254)
    name  = models.CharField(max_length=50)
    text  = models.TextField()
    
    def __str__(self):
        return self.name



