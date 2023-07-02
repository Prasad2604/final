from django.shortcuts import render, HttpResponse
from .models import Cafe

# Create your views here.
def index(request):
    
    return render(request,'index.html')
def shakes(request):
    
    return render(request,'shakes.html')
def cafe(request):
    cafes = Cafe.objects.all()
    print(cafes)
    params={'cafe':cafes}
    return render(request,'cafe.html',params)
def restaurant(request):
    return render(request,'restaurant1.html')
def login(request):
    
    return render(request,'SignIn.html')
def OurTeam(request):
    
    return render(request,'animation.html')
def cart(request):
    

    return render(request, 'order_summery.html')
    

    
    