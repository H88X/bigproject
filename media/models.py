from django.db import models
from agency.models import Agency

class Media(models.Model):
    agency_id = models.ForeignKey(Agency, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name