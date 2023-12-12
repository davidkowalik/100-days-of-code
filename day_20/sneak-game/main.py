from turtle import Screen
from sneak import Sneak
from food import Food
from score import Scoreboard
import time

EASY = 0.2
HARD = 0.1

difficulty_level = input("Choose Your difficulty level (EASY/HARD): ")

if difficulty_level.lower() == "easy":
    dif_lvl = EASY
elif difficulty_level.lower() == "hard":
    dif_lvl = HARD
else:
    print("You moron, You gonna play hell lvl")
    dif_lvl = 0.05


# screen setup 600x600, black
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Sneak Game")
screen.tracer(0)

sneak = Sneak()
food = Food()
scoreboard = Scoreboard()


screen.listen()  # Set focus on TurtleScreen (in order to collect key-events).
screen.onkey(sneak.up, "Up")
screen.onkey(sneak.down, "Down")
screen.onkey(sneak.right, "Right")
screen.onkey(sneak.left, "Left")


screen.update()  # refresh screen (manual refresh)
game_over = False
while not game_over:
    screen.update()  # refresh screen (manual refresh, after all segments are moved to new position)
    time.sleep(0.1)  # wait 100ms
    sneak.move()

    # detect collision with food
    if sneak.head.distance(food) < 15:
        scoreboard.increase_scoreboard()
        sneak.extend()
        food.refresh()

    # detect collision with wall
    if sneak.head.xcor() > 290 or sneak.head.xcor() < -290 or sneak.head.ycor() > 290 or sneak.head.ycor() < -290:
        scoreboard.game_over()
        game_over = True

    # detect collision with tail
    # if head collides with any segment in the tail -> game over
    for seg in sneak.segments[1:]:
        if sneak.head.distance(seg) < 10:
            scoreboard.game_over()
            game_over = True











screen.exitonclick()

