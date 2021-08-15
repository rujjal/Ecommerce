from django.shortcuts import render
from django.views.generic import View
from .models import *
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages

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
		self.views['reviews'] = Review.objects.filter(product = slug)

		return render(request,'product-details.html', self.views)


def review(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		comment = request.POST['comment']
		product = request.POST['product']

		data = Review.objects.create(
			name = name,
			email = email,
			product = product,
			comment = comment
			)
		data.save()

	return redirect(f'/detail/{product}')


def signup(request):
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		cpassword = request.POST['cpassword']
		fname = request.POST['fname']
		lname = request.POST['lname']
		if password == cpassword:
			if User.objects.filter(username = username).exists():
				messages.error(request,'This username is already taken')
				return redirect('home:signup')

			elif User.objects.filter(email = email).exists():
				messages.error(request,'This email is already taken')
				return redirect('home:signup')

			else:
				user = User.objects.create_user(
					username = username,
					email = email,
					first_name = fname,
					last_name = lname,	
					)
				user.save()
				messages.success(request,'You are Signuped!!!')
				return redirect('/')

		else:
			messages.success(request,'You are Signuped!!!')
			return redirect('home:signup')

	return render(request,'signup.html')

class SearchView(BaseViews):
	def get(self,request):
		query = request.GET.get('query')
		if not query:
			return redirect('/')
		self.views['search_product'] = Item.objects.filter(title__icontains = query)

		return render(request,'search.html', self.views)