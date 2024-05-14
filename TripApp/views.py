from django.shortcuts import render, redirect
from TripApp.models import Destination
from TripApp.models import Hotels
from django.views.generic.list import ListView
from . models import Tourpackages
from . models import Restuarants
from . forms import CustomerForm


# Create your views here.
def home(request):
    dests = Destination.objects.all()
    return render(request,'TripApp/home.html',{'dests':dests})

def hotels(request):
    hotels = Hotels.objects.all()
    return render(request,'TripApp/hotels.html',{'hotels':hotels})

def restuarants(request):
    return render(request,'TripApp/restuarants.html')

def tourpackages(request):
    return render(request,'TripApp/tourpackages.html')

def company(request):
    return render(request,'TripApp/company.html')

def flight(request):
    return render(request,'TripApp/flight.html')

def cruise(request):
    return render(request,'TripApp/cruise.html')

def car(request):
    return render(request,'TripApp/car.html')

def navbar(request):
    return render(request,'TripApp/navbar.html')

def search_results(request):
    query = request.GET.get('query')
    results = Hotels.objects.filter(hlocation=query)  # Adjust this query based on your model fields
    return render(request, 'TripApp/search_results.html', {'results': results})

class Package_list(ListView):
    model = Tourpackages
    template_name = 'TripApp/tourpackages.html'
    context_object_name = 'package'

class Restuarant_list(ListView) :
    model =  Restuarants
    template_name = 'TripApp/restuarants.html'
    context_object_name = 'restuarant'

def product_display(request,id):
    products = Destination.objects.get(id=id) #This is actually for product display . I can't add form submission in this because already one post request is there through id 
    form = CustomerForm
    return render(request,'TripApp/product_display.html', {'products':products,'form':form})

def CustomerData(request):
    form = CustomerForm
    if request.method =='POST': #this is the code for form but unable to work becuse the data is coming from product display
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/')
    return render(request,'TripApp/navbar.html')