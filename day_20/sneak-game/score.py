from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Consolas', 12, 'normal')
GAME_OVER_FONT = ('Consolas', 20, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(0, 280)
        self.score = 0
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Score = {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 150)
        self.write(arg="💀💀 GAME OVER 💀💀", move=False, align=ALIGNMENT, font=GAME_OVER_FONT)

    def increase_scoreboard(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()