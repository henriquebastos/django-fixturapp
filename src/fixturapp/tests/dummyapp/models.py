from django.db import models

class Dummy(Model):
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=250)

