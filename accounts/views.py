from django.shortcuts import render




def signup_view(request):
    
    return render(request, 'accounts/signup.html')

    
def login_view(request):
    if request.user.is_authenticated:
        msg = f'user is authenticated as {request.user.username}'
    else:
        msg = 'user is not authenticated'
    context = {'msg': msg}
    return render(request, 'accounts/login.html', context)

def logout_view(request):
    pass