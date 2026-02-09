from django.shortcuts import render
from .forms import ContactForm
from django.shortcuts import redirect
from django.contrib import messages
from blog.models import Post, category

def index(request):
    posts = Post.objects.filter(status=1)
    categories = category.objects.all()
    context = {'posts': posts, 'categories': categories}
    return render(request,'website/index.html', context)

def about(request):
    return render(request,'website/about.html')

def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully')
            return redirect(request.path)
        else:
            messages.error(request, 'There was an error sending your message')
    form = ContactForm()
    return render(request,'website/contact.html', {'form': form})

def elements(request):
    return render(request,'website/elements.html')
# Create your views here.
