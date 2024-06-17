# create a snake body
# move the snake
# control the snake

"""first set up the environment for the snake game.."""
from turtle import Turtle, Screen
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game😎')
screen.tracer(0)

# TODO.1 Create a Snake Body
# x_range = [-20, -40, -60] or
position = [(0, 0), (-20, 0), (-40, 0)]

new_turtle = []
for turtle in position:
    tim = Turtle('square')
    tim.color('white')
    tim.penup()
    tim.goto(turtle)
    new_turtle.append(tim)

# TODO.2 Automatically move the snake, but find a way to change the direction
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(new_turtle) - 1,0, -1):
        new_x = new_turtle[seg_num-1].xcor()
        new_y = new_turtle[seg_num-1].ycor()
        new_turtle[seg_num].goto(new_x, new_y)
    new_turtle[0].forward(20)