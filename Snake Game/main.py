### Snake Game ###
"""
Break down the problem
1). Create a snake body
2). Move the snake
3). Control the snake
4). Detect collision with food
5). Create a scoreboard
6). Detect collision with wall
7). Detect collision with tail
"""

import time
from turtle import Turtle, Screen
from snake import Snake
from scoreboard import Scoreboard
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Upgrade Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.go_up, "Up")
screen.onkey(snake.go_down, "Down")
screen.onkey(snake.go_left, "Left")
screen.onkey(snake.go_right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        food.spawn()
        snake.extend()
        scoreboard.score_increase()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 15:
            scoreboard.reset()
            snake.reset()



screen.exitonclick()
