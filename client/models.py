from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=20)

    def __str__(self):
        return self.name
