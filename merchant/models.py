from django.db import models

# Create your models here.

class Product(models.Model):
	product_id = models.CharField(max_length=200,unique=True)
	name = models.CharField(max_length=200)
	describ = models.CharField(max_length=200)
	url = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=5,decimal_places=2)
	amount = models.PositiveIntegerField()
	remnant = models.PositiveIntegerField()
	site = models.CharField(max_length=200)
	classify = models.CharField(max_length=200)
	merchant_id = models.PositiveIntegerField()
	def __unicode__(self):
		return u'%s,%s' %(self.name,self.describ)
		#return [self.name,self.describ]
