from turtle import Turtle,Screen

tim=Turtle()
screen=Screen()
screen.listen()
def forwored ():
    tim.forward(10)
def backwords():
    tim.backward(10)
def counter():
    new_heading=tim.heading()+10
    tim.setheading(new_heading)
def notclockwise():
    new_heading=tim.heading()-10
    tim.setheading(new_heading)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
screen.onkey(key="A",fun=counter)
screen.onkey(key="W",fun=forwored)
screen.onkey(key="S",fun=backwords)
screen.onkey(key="D",fun=notclockwise)
screen.onkey(key="C",fun=clear)
screen.exitonclick()