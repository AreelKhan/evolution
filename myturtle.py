from turtle import Turtle

class MyTurtle(Turtle):
    def __init__(self, color, pensize, shape, speed):
        super().__init__(shape)
        self.color(color)
        self.pensize(pensize)
        self.speed(speed)
