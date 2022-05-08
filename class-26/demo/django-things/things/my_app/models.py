from django.db import models


class Thing(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class CoolThing(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    is_cool = models.BooleanField()

    def __str__(self):
        return self.name