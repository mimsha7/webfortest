from django.db import models

# Create your models here.
class Contact(models.Model):
     name = models.CharField(max_length=155, null=True)
     email = models.EmailField()
     address = models.CharField(max_length=254)
     city = models.CharField(max_length=150)
     zipcode = models.CharField(max_length=15)
