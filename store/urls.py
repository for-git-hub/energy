from . import  views
from django.urls import path

urlpatterns = [
    path('', views.store, name='store'),
    path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
]