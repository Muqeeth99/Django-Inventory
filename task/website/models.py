from django.db import models

class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=50)
	Quantity_in_stock =  models.CharField(max_length=50)
	Cost_per_item =  models.CharField(max_length=100)
	Sales_made = models.CharField(max_length=50)
	Warehouse =  models.CharField(max_length=150)
	city =  models.CharField(max_length=50)
	state =  models.CharField(max_length=50)
	zipcode =  models.CharField(max_length=20)

	def __str__(self):
		return(f"{self.first_name} {self.last_name}")
