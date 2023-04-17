from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 15, 'normal')


class Scoreboard:

    def __init__(self):
        self.score = 0
        self.score_turtle = Turtle()
        self.score_turtle.pencolor("white")
        self.score_turtle.penup()
        self.score_turtle.goto(0, 280)
        self.score_turtle.hideturtle()

    def write_score(self):
        self.score_turtle.clear()
        self.score_turtle.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.score_turtle.goto(0, 0)
        self.score_turtle.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increment_score(self):
        self.score += 1
