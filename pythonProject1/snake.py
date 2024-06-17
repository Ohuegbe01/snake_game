# TODO.3 Creating "main.py" using a snake class instead
from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]

MOVE_DISTANCE = 20
RIGHT = 0
LEFT = 180
UP = 90
DOWN = 270

class Snake:

    def __init__(self):
        self.new_turtle = []
        self.create_snake()
        self.head = self.new_turtle[0]

    def create_snake(self):
        for turtle in STARTING_POSITIONS:
            self.add_segment(turtle)

    def add_segment(self, turtle):
        tim = Turtle('square')
        tim.color('white')
        tim.penup()
        tim.goto(turtle)
        self.new_turtle.append(tim)

    def extend(self):
        self.add_segment(self.new_turtle[-1].position())

    def move(self):
        for seg_num in range(len(self.new_turtle) - 1, 0, -1):
            new_x = self.new_turtle[seg_num - 1].xcor()
            new_y = self.new_turtle[seg_num - 1].ycor()
            self.new_turtle[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        # self.positioning()

    def upwards(self):
        if self.new_turtle[0].heading() != DOWN:
            self.head.setheading(UP)

    def downwards(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def leftwards(self):
        if self.head.heading() != RIGHT:
            self.new_turtle[0].setheading(LEFT)

    def rightwards(self):
        if self.head.heading() != LEFT:
            self.new_turtle[0].setheading(RIGHT)

    def reset(self):
        for seg in self.new_turtle:
            seg.goto(1080, 1080)
        self.new_turtle.clear()
        self.create_snake()
        self.head = self.new_turtle[0]

