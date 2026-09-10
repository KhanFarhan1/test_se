# Fitness Tracker - Version 2.0
# Features: steps, calories, workout tracking, fitness goals

steps = 0
workouts = []

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

def add_workout(workout, duration):
    workouts.append((workout, duration))
    print(workout, "workout added for", duration, "minutes")

def show_workouts():
    print("Workouts:", workouts)

def set_fitness_goal(goal):
    print("Fitness goal set:", goal)
