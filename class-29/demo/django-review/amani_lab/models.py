from django.db import models


class Thing(models.Model):
    title = models.CharField(max_length=255)

    desc = models.TextField

    def __str__(self):
        return self.title
