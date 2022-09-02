from django.db import models

class Child(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

class Child2(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    
class Child3(models.Model):
    firstName = models.CharField(max_length=256)
    lastName = models.CharField(max_length=256)
    cricketTeam = models.CharField(max_length=256)
    role = models.CharField(max_length=256)