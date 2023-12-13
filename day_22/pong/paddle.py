from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270

class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.speed("fastest")
        self.goto(pos)


    def set_position(self, x):
        pos = (x, 0)
        self.goto(pos)

    def up(self):
        if self.ycor() <= 250:
            y_cord = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(), y_cord)

    def down(self):
        if self.ycor() >= -250:
            y_cord = self.ycor() - MOVE_DISTANCE
            self.goto(self.xcor(), y_cord)