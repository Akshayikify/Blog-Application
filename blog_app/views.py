from django.shortcuts import render,redirect
from .forms import UserRegistrationForm
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
def Login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            form=login(request,user)
            messages.success(request,f'welcome {username}!!')
            return redirect('home')
        else:
            messages.info(request,f'{username} does not exist. Please sign up.')
    form=AuthenticationForm()
    return render(request,'login.html',{'form':form,'title':'login'})
            
def register(request):
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'Your account has been successfully created! Now you can login')
            return redirect('login')
    else:
        form=UserRegistrationForm()
    return render(request,'register.html',{'form':form,'title':'Register'})
        
def home(request):
    return render(request,'index.html',{'title':'home'})

