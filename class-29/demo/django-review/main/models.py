from django.db import models


class Item(models.Model):
    name= models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    def __str__(self):
        return self.name


class Meal(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
