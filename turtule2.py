from turtle import Turtle,Screen
import random
tim=Turtle()
tim.shape("turtle")

light_colors = [
    "#FFB6C1",  # Light Pink
    "#FFDAB9",  # Peach Puff
    "#FFE4E1",  # Misty Rose
    "#FFFACD",  # Lemon Chiffon
    "#E6E6FA",  # Lavender
    "#F0FFF0",  # Honeydew
    "#F5FFFA",  # Mint Cream
    "#F0F8FF",  # Alice Blue
    "#F5F5DC",  # Beige
    "#FFF0F5",  # Lavender Blush
    "#FAFAD2",  # Light Goldenrod Yellow
    "#FFEFD5",  # Papaya Whip
    "#FFFFE0",  # Light Yellow
    "#F8F8FF",  # Ghost White
    "#F0FFFF",  # Azure
    "#FDF5E6",  # Old Lace
    "#FFFAF0",  # Floral White
    "#FFF5EE",  # Seashell
    "#FFF8DC",  # Cornsilk
    "#FAEBD7",  # Antique White
    "#FFFACD",  # Lemon Chiffon
    "#FFEBCD",  # Blanched Almond
    "#FFDAB9",  # Peach Puff
    "#FFE4B5",  # Moccasin
    "#FFDEAD",  # Navajo White
    "#FFE4C4",  # Bisque
    "#FFEBCD",  # Blanched Almond
    "#FFFFF0",  # Ivory
    "#FFF0F5",  # Lavender Blush
    "#FFFAFA"   # Snow
]
directions=[0,90,180,270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(100):
    tim.color(random.choice(light_colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))






screen=Screen()
screen.exitonclick()