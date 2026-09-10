# Fitness Tracker - Version 1.0
# Features: record and display daily steps

steps = 0

def add_steps(count):
    global steps
    steps += count
    print("Steps recorded:", steps)

def show_steps():
    print("Total steps:", steps)
