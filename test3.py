import turtle

from turtle import Turtle, Screen
from myturtle import MyTurtle
from random import randint, choice

WIDTH, HEIGHT = 500, 500
RADIUS = 5
NUM_DOTS = 50
BOUNDS = {
    "left":RADIUS - WIDTH//2,
    "right":WIDTH//2 - RADIUS,
    "top":HEIGHT//2 - RADIUS,
    "bottom":RADIUS - HEIGHT//2,
}

screen = Screen()
screen.setup(WIDTH, HEIGHT)
turtle.title("Evolution Simulation")

t = Turtle(visible=False)
a = Turtle(visisble=False)

for _ in range(NUM_DOTS):

    t.setposition(x, y)
    a.setposition(y, x)

    t.dot(RADIUS * 2, 'black')
    t.dot(RADIUS * 2, 'black')

screen.exitonclick()
