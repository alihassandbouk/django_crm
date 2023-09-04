from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .models import Record
from django.contrib import messages
from .forms import SignUpForm

# Create your views here.
def home(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        #Autinticate user
        user = authenticate(request,username= username, password = password)
        if user is not None:
            login(request,user)
            messages.success(request,"Your have logged in")
            return redirect('website:home') 
        else:
            messages.success(request,"There was an error logginig in!!")
            return redirect('website:home')

    else:
        return render(request,'home.html',{
    
    })


def logout_user(request):
    logout(request)
    return redirect("website:home")


def register(request):
    
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate and log in
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(request,username=username,password=password)
            login(request,user)
            messages.success(request,"Your are logged in!!")
            return redirect('website:home')
        else:
            messages.success(request,"something wrong happended")
            return redirect('website:register')
    else:
        form = SignUpForm()
        return render(request,'register.html',{
            "form":form
        })