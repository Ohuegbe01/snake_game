# TODO 4. adding a snake class into the new main.py
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game😎')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# TODO 5. creating a listener to interact with the object through keys
screen.listen()
screen.onkey(snake.upwards, 'Up')
screen.onkey(snake.downwards, 'Down')
screen.onkey(snake.leftwards, 'Left')
screen.onkey(snake.rightwards, 'Right')


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

#   TODO.7 detecting collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        # TODO 10. extending the body
        snake.extend()
        scoreboard.increase_score()
    # TODO 9. detecting collisions with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

# TODO 11. Detecting collisions with the body or tail
        for turtle in snake.new_turtle[1:]:
            if snake.head.distance(turtle) < 10:
                scoreboard.reset()
                snake.reset()

screen.exitonclick()