from django.shortcuts import render, redirect
from .form import SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def signup(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/signin')
    else:
        form=SignUpForm()
    return render(request, 'signup.html', {'form':form})

def signin(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/home')
    else:
        form=AuthenticationForm()
    return render(request, 'signin.html', {'form':form})

def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return redirect('/signin')
    
def signout(request):
    logout(request)
    return redirect('/signin')