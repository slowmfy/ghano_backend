from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import todo
from django.contrib.auth.decorators import login_required

def register(request):
    if request.user.is_authenticated:
        return redirect('home-page')
    if request.method == 'POST':
        # Get data from the form
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')  # Fetch first name
        last_name = request.POST.get('last_name')    # Fetch last name

        # Validate password length
        if len(password) < 3:
            messages.error(request, 'Password must be at least 3 characters.')
            return redirect('register')

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Error: Username already exists, use another.')
            return redirect('register')

        # Create a new user
        new_user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,  # Save first name
            last_name=last_name     # Save last name
        )
        new_user.save()

        # Success message
        messages.success(request, 'User successfully created, login now.')
        return redirect('login')

    # Render the registration page
    return render(request, 'todoapp/register.html', {})



def loginpage(request):
    
    if request.user.is_authenticated:
        return redirect('home-page')
    
    
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        validate_user=authenticate(username=username,password=password)
        if validate_user is not None:
            login(request,validate_user)
            return redirect('home-page')
        else:
            messages.error(request,'Error,User Details o user does not eixsts')
            return redirect('login')
            
            
        
    
    
    return render(request,'todoapp/login.html',{})
def LogoutView(request):
    logout(request)
    return redirect('login')

