from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('showroom/', views.showroom, name='showroom'),
    path('showroom/<slug:slug>/', views.product_detail, name='product_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
