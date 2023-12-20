from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

X_UP = 10
X_DOWN = -10
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# screen initialization
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title('PONG')
screen.tracer(0)

# initialize right paddle
r_paddle = Paddle(pos=(350,0))

# initialize left paddle
l_paddle = Paddle(pos=(-350,0))

# initialize ball
ball = Ball()

# initialize scoreboard
score = Scoreboard()


screen.listen()  # Set focus on TurtleScreen (in order to collect key-events).
# initialize movement of right paddle
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")

# initialize movement of left paddle
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")


screen.update()  # refresh screen (manual refresh)
game_over = False

while not game_over:
    screen.update()  # refresh screen (manual refresh, after all segments are moved to new position)
    time.sleep(ball.ball_move_speed)  # wait 100ms

    ball.move()
    # detect collision with top and bottom wall
    if ball.ycor() >= (SCREEN_HEIGHT/2 - 10) or ball.ycor() <= -(SCREEN_HEIGHT/2 - 10):
        ball.y_bounce()

    # detect collision with paddle
    if ball.xcor() > 320 and r_paddle.distance(ball) < 50 or ball.xcor() < -320 and l_paddle.distance(ball) < 50:
        ball.x_bounce()

    if ball.xcor() > 380:
        score.increase_l_score()
        ball.reset_ball()

    if ball.xcor() < -380:
        score.increase_r_score()
        ball.reset_ball()


















screen.exitonclick()