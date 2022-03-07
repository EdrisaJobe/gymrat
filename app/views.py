from django.shortcuts import render, redirect
from .forms import Register
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
import requests
from .calories import BMR, TEF, Exercise_Energy_Expenditure, Non_Exercise_Activity_Thermogenesis, Total_Daily_Energy_Expenditure, recommended_calories

### HOMEPAGE ###
def index(request):

    return render(request, 'index.html')

### Calories ###
def calories(request):
    
    # inputs for user prompt, wehn submitted post results
    if request.method == "POST":
        weight = int(request.POST['weight'])
        goal = int(request.POST['goal'])
        workout = request.POST['workout']
        activity_level = request.POST['activity_level']
        
        # setting up variables for each function within calories.py
        bmr = BMR(weight)
        tef = TEF(bmr)
        EEE = Exercise_Energy_Expenditure(workout)
        NEAT = Non_Exercise_Activity_Thermogenesis(activity_level)
        TDEE = Total_Daily_Energy_Expenditure(bmr, tef, EEE, NEAT)
        rc = recommended_calories(TDEE, goal, weight)
        
        # setting variables for calculation type
        lose_half = rc[0]
        lose_one = rc[1]
        time_to_lose_half = rc[2]
        time_to_lose_one = rc[3]
        
        # context, returning the values
        return render(request, "calories.html", {
            "bmr": bmr,
            "Total_Daily_Energy_Expenditure": TDEE,
            # "rate": rate,
            "lose_half": lose_half,
            "lose_one": lose_one,
            # "lose_one_half": lose_one_half,
            # "lose_two": lose_two,
            "goal": goal,
            "time_to_lose_half": time_to_lose_half,
            "time_to_lose_one": time_to_lose_one,
            # "time_to_lose_one_half": time_to_lose_one_half,
            # "time_to_lose_two": time_to_lose_two,
        })
    else:
        return render(request, "calories.html")

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
                messages.error(
                    request, 'Invalid username or password, try again.')
                return redirect('main:login')
        else:
            messages.error(request, 'Invalid username or password, try again.')
            return redirect('main:login')
    form = AuthenticationForm()

    return render(request, 'login.html', context={"login_form": form})

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
