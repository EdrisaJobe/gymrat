from django.shortcuts import render, redirect
from .forms import Register
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


### HOMEPAGE ###
def index(request):
    
    return render(request, 'index.html')

### LOGIN FORM ###
def login_form(request):
    
    # when user attempts to login promt user and pass inputs.
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        
        # if the form is correct, save the information
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            # verifies user cardentials and returns object in database
            user = authenticate(username=username, password=password)
            
            # if user successfully enters info, promt with success.
            if user is not None:
                auth_login(request, user)
                messages.info(request, f'Now logged in as {username}.')
                return redirect('main:home')
            
            # wrong password or username error
            else:
                messages.error(request, 'Invalid username or password, try again.')
                return redirect('main:login')
        else:
            messages.error(request, 'Invalid username or password, try again.')
            return redirect('main:login')
    form = AuthenticationForm()
    
    return render(request, 'login.html', context={"login_form":form})

### REGISTER FORM ###
def register(request):
    
    # when user submit the form, prompt with whether or not it was successful
    if request.method == "POST":
        form = Register(request.POST)
        
        # check form validation then saving the info
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, "Successfully registered!")
            return redirect("main:login")

        # if not valid, raise an error
        messages.error(request, "Unsuccessful, invalid information given.")
    form = Register()
    
    return render(request, 'register.html', context={"register": form})