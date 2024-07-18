from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('about/',views.about, name='about'),
    path('testimonial/',views.testimonial, name='testimonial'),
    path('product/',views.Product, name='product'),
    path('contact/',views.contact, name='contact')

]
