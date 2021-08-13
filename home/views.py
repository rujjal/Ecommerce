from django.shortcuts import render
from django.views.generic import View
from .models import *

# Create your views here.


class BaseViews(View):
	views = {}
	views['category'] = Category.objects.all()
	views['subcategory'] = SubCategory.objects.all()

class HomeView(BaseViews):
	def get(self, request):
		self.views['items'] = Item.objects.filter(labels = 'hot')
		self.views['sale_items'] = Item.objects.filter(labels = 'sale')
		self.views['slider'] = Slider.objects.all()
		self.views['ad'] = Ad.objects.all()

		return render(request, 'index.html', self.views)

class SubCategoryView(BaseViews):
	def get(self,request,slug):
		slug_id = SubCategory.objects.get(slug = slug).id
		self.views['subcat_items'] = Item.objects.filter(subcategory_id = slug_id)

		return render(request,'subcat.html', self.views)

class ProductDetailView(BaseViews):
	def get(self,request,slug):
		self.views['details'] = Item.objects.filter(slug = slug)


		return render(request,'product-details.html', self.views)
