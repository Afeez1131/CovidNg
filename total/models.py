from django.db import models
from datetime import datetime
# Create your models here.


class Total(models.Model):
	sample = models.CharField(max_length=200)
	confirmed = models.CharField(max_length=200)
	active = models.CharField(max_length=200)
	discharged = models.CharField(max_length=200)
	death = models.CharField(max_length=200)

	def __str__(self):
		return self.confirmed


# class TotalDate(models.Model):
# 	date = models.DateTimeField(default=datetime.now, blank=True)
# 	sample = models.CharField(max_length=200, null=True)
# 	confirmed = models.CharField(max_length=200, null=True)
# 	active = models.CharField(max_length=200, null=True)
# 	discharged = models.CharField(max_length=200, null=True)
# 	death = models.CharField(max_length=200, null=True)

# 	def __str__(self):
# 		return str(self.date)[:10]