from django.db import models

# Create your models here.
class Advertising(models.Model):
    Tv = models.FloatField()
    Radio = models.FloatField()
    Newspaper = models.FloatField()
