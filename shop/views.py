from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def testimonial(request):
    return render(request,'testimonial.html')
def Product(request):
    return  render(request,'product.html')
def contact(request):
    return render(request,'contact.html')

