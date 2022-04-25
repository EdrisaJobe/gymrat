import requests

### Login/Register form imports
from django.shortcuts import render, redirect
from .forms import Register
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

### Calories imports
from .calories import BMR, TEF, Exercise_Energy_Expenditure, Non_Exercise_Activity_Thermogenesis, Total_Daily_Energy_Expenditure, recommended_calories

### Dashboard imports
from .models import LogWorkout
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

### DASHBOARD ###
class Workout(ListView):
    
    model = LogWorkout
    context_object_name = 'log'
    template_name = 'app/dashboard.html'
    
class AddWorkout(CreateView):
    
    model = LogWorkout
    fields = ['current_date','workout_type','weights','reps']
    success_url = reverse_lazy('main:home')
    template_name = 'app/logworkout.html'

class UpdateWorkout(UpdateView):
    
    model = LogWorkout
    fields = ['current_date','workout_type','weights','reps']
    success_url = reverse_lazy('main:home')
    template_name = 'app/logworkout.html'

class DeleteWorkout(DeleteView):
    
    model = LogWorkout
    context_object_name = 'log'
    success_url = reverse_lazy('main:home')
    template_name = 'app/delete.html'
    
    # def index(request):
        
    #     if request.method == "POST":
            
    #         # logs user prompt based on the following
    #         workout = request.POST['workout_type']
    #         weight = int(request.POST['weights'])
    #         reps = int(request.POST['reps'])
        
    #         return render(request, 'index.html', {
    #                                             "workout": workout,
    #                                             "weight":weight,
    #                                             "reps":reps})
    #     else:
    #         return render(request, 'index.html')

### Facts page ###
def facts(request):
    
    return render(request, 'facts.html')

### Motivation Page ###
def motivation(request):
    
    return render(request, 'motivation.html')

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

### RECIPES PAGE ###
def recipes(request):
    
    return render(request, 'recipes.html')

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
