from . import  views
from django.urls import path

urlpatterns = [
    path('about/', views.about, name='about'),
    path('partners/', views.partners, name='partners'),
    path('contact/', views.contact, name='contact'),

]