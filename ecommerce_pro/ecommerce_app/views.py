from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from ecommerce_app.forms import UserRegistrationForm
from ecommerce_app.models import product


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid username or password.'
    else:
        error_message = None

    return render(request, 'login.html', {'error_message': error_message})
def logout_user(request):
    logout(request)
    return redirect('login')

def display(request):
    product1 = product.objects.all()
    context = {
        'product_list':product1
    }
    return render(request, 'product.html', context)

def home(request):
    return render(request,'home.html', {'userName' : request.user.username})
def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration.html', {'form': form})