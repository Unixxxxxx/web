from django.shortcuts import render, redirect
def home(request):
    return render(request,'home.html',{})

def contact(request):
    return render(request,'contact.html', {})

def About(request):
    return render(request,'About.html', {})

def Services(request):
    return render(request,'Services.html', {})

# component
def ne(request):
    return render(request,'ne.html',{})






# Create your views here.
