from django.db import models
from django.db.models import CASCADE

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)

class Measurement(models.Model):
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    sensor = models.ForeignKey(Sensor, related_name='measurements', on_delete=CASCADE)