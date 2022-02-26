from django.db import models

# Create your models here.


class ElasticDemo(models.Model):
	productname=models.CharField(max_length=200)
	productprice=models.IntegerField()
	quantity=models.IntegerField()

	def __str__(self):
		return self.productname
