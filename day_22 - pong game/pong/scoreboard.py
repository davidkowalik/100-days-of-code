from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Consolas', 40, 'normal')
GAME_OVER_FONT = ('Consolas', 20, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.r_score = 0
        self.l_score = 0
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(x=-200,y=250)
        self.write(arg=f"{self.l_score}", move=False, align=ALIGNMENT, font=FONT)
        self.goto(x=200, y=250)
        self.write(arg=f"{self.r_score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_l_score(self):
        self.l_score += 1
        self.update_scoreboard()

    def increase_r_score(self):
        self.r_score += 1
        self.update_scoreboard()
