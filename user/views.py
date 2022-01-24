from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponseRedirect
from django.urls import  reverse
from django.contrib.auth.decorators import login_required
from .forms import SignUp_form

# Create your views here.
def sign_up(request):
    form = SignUp_form()
    registered = False

    if request.method == 'POST':
        form = SignUp_form(data=request.POST)

        if form.is_valid():
            form.save()
            registered = True
            return render(request, "user/login.html")

        
    dict = {'form':form,'registered':registered}
    return render(request,'user/register.html',context=dict)


def sign_in(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)

            return HttpResponseRedirect(reverse('product:product'))
            
        else:
            messages.error(request, "Bad Credentials!!")
            
            
    
    return render(request, "user/login.html")

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('user:login'))