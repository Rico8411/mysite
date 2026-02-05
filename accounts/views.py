from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse




# Create your views here.


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return redirect('accounts:login')
    else:
        return redirect('/')

    return render(request, 'accounts/login.html')

@login_required #if user is logged in they can logout
def logout_view(request):
    logout(request)
    return redirect('/')

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(reverse('accounts:login'))
        form = UserCreationForm()
        context = {'form':form}
        return render(request, 'accounts/signup.html', context)
    else:
        return redirect('/')