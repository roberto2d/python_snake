from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self) -> object:
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.shape("square")
        #self.shapesize(0.5)
        self.color("yellow")
        self.respawn()

    def respawn(self):
        self.goto(randint(-24, 24) * 20, randint(-14, 14) * 20)

    def erase(self):
        self.goto(1000,1000)
