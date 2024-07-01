from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import CustomUserCreationForm

def index(request):
    return render(request, 'index.html')

def login_user(request, template_name, dashboard_redirect, user_type):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and getattr(user, f'is_{user_type.lower()}'):
                login(request, user)
                return redirect(dashboard_redirect)
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, template_name, {'form': form})

def patient_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_patient:
                login(request, user)
                return redirect('patient_dashboard')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'patient_login.html', {'form': form})

def doctor_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_doctor:
                login(request, user)
                return redirect('doctor_dashboard')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'doctor_login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. Please login.')
            return redirect('index')  # Redirect to the home page after signup
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def patient_dashboard(request):
    if request.user.is_authenticated and request.user.is_patient:
        context = {
            'title': 'Patient Dashboard',
            'welcome_message': 'Welcome to your patient dashboard!',
            # Add more data as needed
        }
        return render(request, 'patient_dashboard.html', context)
    else:
        return redirect('patient_login')

def doctor_dashboard(request):
    if request.user.is_authenticated and request.user.is_doctor:
        context = {
            'title': 'Doctor Dashboard',
            'welcome_message': 'Welcome to your doctor dashboard!',
            # Add more data as needed
        }
        return render(request, 'doctor_dashboard.html', context)
    else:
        return redirect('doctor_login')

def logout_view(request):
    logout(request)
    return redirect('index')

