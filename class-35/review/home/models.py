from django.db import models

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=255)
    details = models.TextField(default="Place something here")
    is_cool = models.BooleanField(default= True)
    image = models.ImageField(null = True, blank = True)

    def __str__(self):
        return self.title
