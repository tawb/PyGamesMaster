
from turtle import Turtle,Screen
import random
from random import randint
tim=Turtle()
tim.shape("turtle")
pink_shades = [
    "#FFC0CB",  # Pink
    "#FFB6C1",  # Light Pink
    "#FF69B4",  # Hot Pink
    "#FF1493",  # Deep Pink
    "#DB7093",  # Pale Violet Red
    "#C71585",  # Medium Violet Red
    "#FF87B2",  # Ultra Pink
    "#FF6FFF",  # Shocking Pink
    "#FBAED2",  # Amaranth Pink
    "#E75480",  # Dark Pink
    "#F5A9BC",  # Pastel Pink
    "#E68FAC",  # Light Hot Pink
    "#FFDFDD",  # Very Pale Pink
    "#D94F70",  # Dark Carnation Pink
    "#FF91AF",  # Salmon Pink
    "#FFD1DC",  # Baby Pink
    "#FF85B2",  # French Pink
    "#FF6F91",  # Paradise Pink
    "#F88379",  # Coral Pink
    "#FF5A77",  # Fiery Pink
]
tim.speed("fastest")
def draw(size):

    for _ in range(int(360/size)):
        tim.color(random.choice(pink_shades))
        tim.circle(50)
        current_heading=tim.heading()
        tim.setheading(current_heading+10)
        




draw(5)




screen=Screen()
screen.exitonclick()