# from turtle import Turtle, Screen
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreBoard = Scoreboard()
game_is_on = True

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect food
    if (snake.head.distance(food) < 15):
        food.refresh()
        snake.extend()
        scoreBoard.increase_score()

    # Detect wall
    if (snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280):
        scoreBoard.game_over()
        game_is_on = False

    # Detect tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif (snake.head.distance(segment) < 10):
            game_is_on = False
            scoreBoard.game_over()

screen.exitonclick()
