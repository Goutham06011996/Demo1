
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib import messages,auth



# Create your views here.
def Login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            print("Invalid Credentials")
            messages.info(request,"Invalid Credentials")
            return redirect('Login')

    return render(request,"Login.html")

def logout(request):
    auth.logout(request)
    print("Logout Successfull")
    return redirect('/')

