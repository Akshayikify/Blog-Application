from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=20)
    description=models.TextField()
    image=models.ImageField(upload_to='products/')
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name