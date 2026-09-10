# Fitness Tracker - Version 1.1
# Features: step tracking and calorie calculation

steps = 0

def add_steps(count):
    global steps
    steps += count
    print("Steps recorded:", steps)

def show_steps():
    print("Total steps:", steps)

def calculate_calories(steps, calories_per_step=0.04):
    calories = steps * calories_per_step
    print("Calories burned:", calories)
    return calories
