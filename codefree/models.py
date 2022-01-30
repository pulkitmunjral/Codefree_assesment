from django.db import models

# Create your models here.
class flower(models.Model):
    Class = models.TextField()
    Sepal_length = models.FloatField()
    Sepal_width = models.FloatField()
    Petal_length = models.FloatField()
    Petal_width = models.FloatField()

