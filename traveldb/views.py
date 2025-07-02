from django.shortcuts import render, redirect
from .models import Service 
from .forms import ContactForm

def home(request):
    return render(request,'home.html',{})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')  # Redirect after successful submission
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def About(request):
    return render(request,'About.html', {})

def services_view(request):
    services = Service.objects.all()
    return render(request, 'Services.html', {'services': services})

# component
def ne(request):
    return render(request,'ne.html',{})






# Create your views here.
