from django.db import models

class Person(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	class Car(models.Model):
		#consdering using a foreign key not sure what its for
		#I want the cars to relate to the person



