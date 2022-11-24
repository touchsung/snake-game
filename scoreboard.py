from turtle import Turtle

class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.score = 0
    self.color("white")
    self.penup()
    self.goto(0, 270)
    self.hideturtle()
    self.update_score()

  def increase_score(self):
    self.score += 1
    self.clear()
    self.update_score()

  def update_score(self):
    self.write(f"Score: {self.score}", align="center", font=("Arial", 12, "normal"))

  def game_over(self):
    self.clear()
    self.goto(0, 0)
    self.write("GAMEOVER", align="center", font=("Arial", 24, "normal"))
    self.goto(0, -20)
    self.write(f"Your score is {self.score}", align="center", font=("Arial", 12, "normal"))