from django.db import models

# Create your models here.
class CartItems(models.Model):
    product_name = models.CharField(max_length=255)
    product_price = models.FloatField()
    product_quantity = models.PositiveIntegerField()
    
    
class CricketTeamSheet(models.Model):
    firstName = models.CharField(max_length=256)
    lastName = models.CharField(max_length=256)
    cricketTeam = models.CharField(max_length=256)
    role = models.CharField(max_length=256)
    
