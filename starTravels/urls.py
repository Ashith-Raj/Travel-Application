"""
URL configuration for starTravels project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from TripApp import views

urlpatterns = [
     path('',views.home,name="home"),
     path('admin/', admin.site.urls),
     path('hotels/',views.hotels,name="hotels"),
     path('restuarants/',views.Restuarant_list.as_view(),name="restuarants"),
     path('company/',views.company,name="company"),
     path('tourpackages/',views.Package_list.as_view(),name="tourpackages"),
     path('flight/',views.flight,name="flight"),
     path('cruise/',views.cruise,name="cruise"),
     path('car/',views.car,name="car"),
     path('navbar/',views.CustomerData,name="form"),
     path('search/', views.search_results, name='search_results'),
     path('product_display/<id>',views.product_display,name="product_display"),
     path('purchased/',views.CustomerData,name="purchased")

   
]
# +static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


