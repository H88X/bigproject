# from django.db import models
# from client.models import Client

# class Advertising(models.Model):
#     client = models.ForeignKey(Client, on_delete=models.CASCADE)
#     target_age = models.IntegerField()
#     target_gender = models.CharField(max_length=1)

#     def __str__(self):
#         return f"Advertising for {self.client.name}"

from django.db import models
from common.models import User

class Advertising(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    #client_id = models.IntegerField()
    target_age = models.IntegerField()
    target_gender = models.CharField(max_length=1)
