from turtle import Turtle, Screen
import random

# Set up the screen
screen = Screen()
screen.setup(width=500, height=400)

# Get the user's bet
user_bet = screen.textinput(title="Make your guess", prompt="Which turtle will win the race? (red, orange, yellow, green, blue, purple)")

# Create a list of colors
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

# Create turtles and position them at the starting line
y_positions = [-100, -60, -20, 20, 60, 100]
for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    turtles.append(new_turtle)

# Start the race
race_on = False

if user_bet:
    race_on = True

while race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:  # Check if any turtle has crossed the finish line
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            break

        # Move the turtle a random distance
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

# Close the screen on click
screen.exitonclick()
