# TODO 6. CREATE FOOD AND RANDOMIZE THE FOOD ACROSS THE X AND Y COORDINATES
import random
from turtle import Turtle

"""we inherent Turtle into the food class"""


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed('fastest')
        self.refresh()

    # TODO 8. Create random positions for the food when snake distance is shorter than 15
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
