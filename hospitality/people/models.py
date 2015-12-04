from django.db import models
#SQL databse will have one table for Person
class Person(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	
#SQL will have another database for Cars but cars will have another field
# for a foreign key which references the person in the Person database
class Car(models.Model):
	owner = models.ForeignKey(Person)
	avaliable = models.BooleanField(initial=False)
	def canUseCar(self):
		self.avaliable = True
	

		#consdering using a foreign key not sure what its for
		#I want the cars to relate to the person



