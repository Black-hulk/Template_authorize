from django.db import models

# Create your models here.
class post(models.Model):
    title= models.CharField(max_length=100)
    description= models.TextField()
    date= models.CharField(max_length=2)
    month= models.CharField(max_length=3)
    image= models.ImageField(upload_to='pics')
    category=models.CharField(max_length=200)