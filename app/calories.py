def BMR(weight):
    """Takes away and returns basal metabolic rate - BMR"""
    weight = weight * 0.45359237
    BMR = (weight * 20)
    return round(BMR, 2)


def TEF(BMR):
    """takes away and returns thermic effect of food - TEF"""
    TEF = (BMR * .1)
    return round(TEF, 2)


def Exercise_Energy_Expenditure(workout):
    """Based off Exercise Level, gives energy expenditure"""
    if workout == "low":
        Exercise_Energy_Expenditure = 250
    elif workout== "medium":
        Exercise_Energy_Expenditure = 350
    elif workout == "high":
        Exercise_Energy_Expenditure = 500
    return Exercise_Energy_Expenditure


def Non_Exercise_Activity_Thermogenesis(Activity_Level):
    """Based off lifestyle, gives non-exercise activity thermogenosis"""
    if Activity_Level == "barely":
        Non_Exercise_Activity_Thermogenesis = 250
    elif Activity_Level == "moderate":
        Non_Exercise_Activity_Thermogenesis = 350
    elif Activity_Level == "active":
        Non_Exercise_Activity_Thermogenesis = 500
    return Non_Exercise_Activity_Thermogenesis


def Total_Daily_Energy_Expenditure(BMR, TEF, Exercise_Energy_Expenditure, Non_Exercise_Activity_Thermogenesis):
    """sum of BMR, TEF, Exercise Energy Expenditure, and Non-Exercise Activity Thermogenesis"""
    total_daily_energy_expenditure = BMR + TEF + \
        Exercise_Energy_Expenditure + Non_Exercise_Activity_Thermogenesis
    return round(total_daily_energy_expenditure, 2)


def recommended_calories(total_daily_energy_expenditure, goal, weight):
    # placeholder variable
    need_to_lose = (goal)
    print(need_to_lose)
    # rate values
    lose_half = round(total_daily_energy_expenditure - 250, 2)
    lose_one = round(total_daily_energy_expenditure - 500, 2)
    # array to hold the rate values
    # calulating the time to reach your goal
    time_to_lose_half = (need_to_lose/0.5)*7
    time_to_lose_one = (need_to_lose/1)*7
    # return all the "time to lose" variables to spit back out
    return lose_half, lose_one, time_to_lose_half, time_to_lose_one


bb = BMR(160)
tt = TEF(bb)
energy = Exercise_Energy_Expenditure("low")
active = Non_Exercise_Activity_Thermogenesis("barely")
tdee = Total_Daily_Energy_Expenditure(bb, tt, energy, active)
