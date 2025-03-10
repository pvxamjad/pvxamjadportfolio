from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name



class protfolio(models.Model):
    img = models.ImageField(upload_to="portfolio")
    name = models.CharField(max_length=30)
    category = models.ManyToManyField(Category) 
    url = models.TextField(null=True)

    def __str__(self):
        return self.name



class Contact(models.Model):
    name = models.CharField(max_length=30)
    number = models.CharField(max_length=30)
    email = models.EmailField() 
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name
