from django.db import models
from datetime import datetime

# Create your models here.
class Covid(models.Model):
	states_affected = models.CharField(max_length=200)
	lab_confirmed = models.CharField(max_length = 200)
	admitted = models.CharField(max_length = 200)
	discharged = models.CharField(max_length = 200)
	death = models.CharField(max_length=200)
	
	def __str__(self):
		return self.states_affected

# class StateDate(models.Model):
# 	date = models.DateTimeField(default=datetime.now, blank=True)
# 	states_affected = models.CharField(max_length=200)
# 	lab_confirmed = models.CharField(max_length = 200)
# 	admitted = models.CharField(max_length = 200)
# 	discharged = models.CharField(max_length = 200)
# 	death = models.CharField(max_length=200)
	

# 	def __str__(self):
# 		return str(self.date)[:10]

