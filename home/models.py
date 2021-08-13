from django.db import models
from django.urls import reverse


# Create your models here.

STATUS = (('active','active'),('inactive','inactive'))
STOCK = (('In Stock','In Stock'),('Out of Stock','Out of Stock'))
LABELS = (('new','new'),('hot','hot'),('sale','sale'),('','default'))

class Category(models.Model):
	title = models.CharField(max_length = 300)
	description = models.TextField(blank = True)
	slug = models.CharField(max_length = 500)
	image = models.TextField(blank = True)

	def __str__(self):
		return (self.title)

class SubCategory(models.Model):
	title = models.CharField(max_length = 300)
	category = models.ForeignKey(Category, on_delete = models.CASCADE)
	description = models.TextField(blank = True)
	slug = models.CharField(max_length = 500)
	image = models.TextField(blank = True)

	def __str__(self):
		return (self.title)

	def get_subcat_url(self):
		return reverse("home:subcategory", kwargs = {'slug':self.slug})

class Item(models.Model):
	title = models.CharField(max_length = 300)
	category = models.ForeignKey(Category, on_delete = models.CASCADE)
	subcategory = models.ForeignKey(SubCategory, on_delete = models.CASCADE)
	description = models.TextField(blank = True)
	slug  = models.CharField(max_length = 500)
	image = models.ImageField(upload_to = 'media')
	price = models.IntegerField()
	discounted_price = models.IntegerField()
	status = models.CharField(max_length = 50, choices = STATUS, blank = True)
	stock = models.CharField(max_length = 50, choices = STOCK, blank = True)
	labels = models.CharField(max_length = 50, choices = LABELS, blank = True)

	def __str__(self):
		return (self.title)

	def get_productdetail_url(self):
		return reverse("home:detail", kwargs = {'slug':self.slug})

class Slider(models.Model):
	title = models.CharField(max_length = 300)
	rank = models.IntegerField()
	status = models.CharField(max_length = 300, choices = STATUS, default = False)
	image = models.ImageField(upload_to = 'media', null = True)
	description = models.TextField(blank = True)

	def __str__(self):
		return self.title

class Ad(models.Model):
	title = models.CharField(max_length = 300)
	rank = models.IntegerField()
	description = models.TextField(blank = True)
	image = models.ImageField(upload_to = 'media')

	def __str__(self):
		return self.title


