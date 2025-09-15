from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 != password2:
            messages.error(request, "Passwords don't match!")
            return redirect('accounts:signup')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('accounts:signup')
            
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('accounts:signup')
            
        user = User.objects.create_user(username=username, email=email, password=password1)
        auth_login(request, user)
        messages.success(request, "Account created successfully!")
        return redirect('accounts:login')  # Change to your home URL
    
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('dashboard:prediction')  # Change to your home URL
        else:
            messages.error(request, "Invalid credentials!")
    
    return render(request, 'login.html')

@login_required
def logout(request):
    auth_logout(request)
    messages.success(request, "You've been logged out successfully.")
    return redirect('dashboard:home')