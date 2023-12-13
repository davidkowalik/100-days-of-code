from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.speed("fastest")
        self.x_direction = 1
        self.y_direction = 1
        self.ball_move_speed = 0.1

    def move(self):
        new_x_cor = self.xcor() + 10 * self.x_direction
        new_y_cor = self.ycor() + 10 * self.y_direction
        self.goto(new_x_cor,new_y_cor)

    def y_bounce(self):
        self.y_direction = self.y_direction * -1

    def x_bounce(self):
        self.x_direction = self.x_direction * -1
        self.ball_move_speed *= 0.9

    def reset_ball(self):
        self.x_bounce()
        self.ball_move_speed = 0.1
        self.goto(0, 0)