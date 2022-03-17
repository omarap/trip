from django.db import models
from django.contrib.gis.measure import D, Distance
from math import sin, cos, radians, degrees, acos

# Create your models here.

class Client(models.Model):
	name = models.CharField(max_length=200)
	latitude = models.DecimalField(max_digits=18,decimal_places=10)
	longitude = models.DecimalField(max_digits=18,decimal_places=10)

	def __str__(self):
		return self.name

class Destination(models.Model):
	name = models.CharField(max_length=200)
	latitude = models.DecimalField(max_digits=18,decimal_places=10)
	longitude = models.DecimalField(max_digits=18,decimal_places=10)
	date = models.DateTimeField(auto_now_add=True)
	client = models.ForeignKey(Client, on_delete=models.CASCADE)

	def __str__(self):
		return f"distance measurement"

	
