from django.urls import path
from .views import *

app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('subcategory/<slug>', SubCategoryView.as_view(), name='subcategory'),
    path('detail/<slug>', ProductDetailView.as_view(), name='detail'),
    path('review', review, name='review'),
    path('signup', signup, name='signup'),
]