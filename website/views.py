from django.shortcuts import render
from .forms import ContactForm
from django.shortcuts import redirect

def index(request):
    return render(request,'website/index.html')

def about(request):
    return render(request,'website/about.html')

def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('website:contact')
    form = ContactForm()
    return render(request,'website/contact.html', {'form': form})

def elements(request):
    return render(request,'website/elements.html')
# Create your views here.
