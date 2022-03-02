from django.shortcuts import render, redirect
from .forms import Register
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.
def login(request):
    return render(request, 'index.html')

def register(request):
    
    # when user submit the form, prompt with whether or not it was successful
    if request == "POST":
        form = Register(request.POST)
        
        # check form validation then saving the info
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Successfully registered!")
            return redirect("/")

        # if not valid, raise an error
        messgaes.error(request, "Unsuccessful, invalid information given.")
    form = Register()
    
    return render(request, 'register.html', context={"register": form})