from django.shortcuts import render
from django.contrib.auth import authenticate, login,logout 
from django.contrib import messages


# Create your views here.

def home(request):

    # Check to see if logging in.
    if request.method=='POST':
        username = request.POST['email']
        password = request.POST['passwd']
        return render(request,'home.html',{})
        
    else:

        return render(request,'home.html',{})

    return render(request,'home.html',{})

def login_user(request):

    pass

def logout_user(request):

    pass

