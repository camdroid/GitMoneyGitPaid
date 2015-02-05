from django.db import models

class User(models.Model):
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=20)
	cashMoney = models.IntegerField(default=0)
	def __str__(self):
		return self.username+" has $"+cashMoney