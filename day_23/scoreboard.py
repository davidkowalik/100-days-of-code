from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.current_lvl = 1
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(x=-200,y=250)
        self.write(arg=f"Level: {self.current_lvl}", move=False, align="center", font=FONT)

    def increase_level(self):
        self.current_lvl += 1
        self.update_scoreboard()
