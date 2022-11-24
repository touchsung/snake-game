# from turtle import Turtle, Screen
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreBoard = ScoreBoard()
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
  head = snake.head
  # Detect food
  if (head.distance(food) < 15):
    food.refresh()
    snake.extend()
    scoreBoard.increase_score()

  # Detect wall
  if (head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280):
    scoreBoard.game_over()
    game_is_on = False

  # Detect tail
    for segment in snake.segments:
      if segment == head:
        pass
      elif (head.distance(segment) < 10):
        scoreBoard.game_over()
        game_is_on = False
screen.exitonclick()
