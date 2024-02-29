from django.db import models

class  User(models.Model):     
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    country = models.CharField(max_length=255)  
