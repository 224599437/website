from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # Page from the theme 
    return render(request, 'pages/index.html')

def products_services(request):
    # Page from the theme 
    return render(request, 'pages/malware_visualization/products_and_services.html')

def malwarehome(request):

    # Page from the theme 
    return render(request, 'pages/malware_visualization/main.html')

def ptguihome(request):

    # Page from the theme 
    return render(request, 'pages/pt_gui/main.html')

