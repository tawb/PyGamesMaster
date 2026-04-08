from turtle import Turtle,Screen
import random
from random import randint
tim=Turtle()
tim.shape("turtle")

colors = ["#E52B50", "#317873", "#738678", "#801818", "#0014A8"]

def draw(shape):
    angle=360/shape
    for _ in range(shape):
        tim.forward(100)
        tim.right(angle)
def fullPainting():
    
    for shape in range(3,11):

        tim.color(random.choice(colors))
        
        draw(shape)

fullPainting()










screen=Screen()
screen.exitonclick()