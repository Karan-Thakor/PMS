from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect

from .models import User

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        if email and password:
            user = authenticate(request, email=email, password=password)

            if user is not None:
                auth_login(request, user)

                print('User', user)

                print(request.user)
                print(request.user.is_authenticated)
                return redirect('/')
            
        
    return render(request, 'account/login.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')

        if name and email and password and confirm_password:
            user = User.objects.create_user(name=name, email=email, password=password)

            print('User created:', user)

            return redirect('/login/')
        else:
            print('Something went wrong')

    else:
        print('Just show the form!')
    return render(request, 'account/signup.html')
