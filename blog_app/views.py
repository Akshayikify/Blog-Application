from django.shortcuts import render,redirect,get_object_or_404
from .forms import UserRegistrationForm
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail , EmailMultiAlternatives
from django.template.loader import get_template
from .models import Product
from .forms import ProductForm
import os
from dotenv import load_dotenv
load_dotenv()
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
            username=form.cleaned_data.get('username')
            email=form.cleaned_data.get('email')
            html_temp=get_template('email.html')
            d={'username':username}
            subject,from_mail,to='welcome',os.getenv('HOST_MAIL'),email
            html_content=html_temp.render(d)
            msg=EmailMultiAlternatives(subject,html_content,from_mail,[to])
            msg.attach_alternative(html_content,'text/html')
            msg.send()
            messages.success(request,f'Your account has been successfully created! Now you can login')
            return redirect('login')
    else:
        form=UserRegistrationForm()
    return render(request,'register.html',{'form':form,'title':'Register'})
        
def home(request):
    return render(request,'index.html',{'title':'home'})

def product_list(request):
    products=Product.objects.all()
    return render(request,'index.html',{'products':products})
def product_detail(request,pk):
    product=Product.objects.get(pk=pk)
    return render(request,'index2.html',{'product':product})
def edit_product(request,pk):
    product=get_object_or_404(Product,pk=pk)
    if request.method=='POST':
        form=ProductForm(request.POST,instance=pk)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form=ProductForm(instance=pk)
    return render(request,'index2.html',{'form':form})
            
def delete_product(request,pk):
    product=get_object_or_404(Product,pk=pk)
    if request.method=='POST':
        product.delete()
        return redirect('product_list')
    return render(request,'delete.html',{'product':product})
    
