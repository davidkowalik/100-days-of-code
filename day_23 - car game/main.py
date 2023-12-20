import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

"""
#1 - TODO - generowanie żółwia i poruszanie sie żółwiem - DONE
#2 - TODO - generowanie ruchu uliczniego - DONE
#3 - TODO - detekcja kolizji
#4 - TODO - sprawdzanie czy zółw przeszedł poziom
#5 - TODO - generowanie poziomów, zmiana poziomu trudności
"""


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# initialize player turtle
player = Player()

# initialize keyboard move Up function
screen.listen()
screen.onkeypress(player.move, "Up")

traffic = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    traffic.move_traffic(scoreboard.current_lvl - 1)
    for car in traffic.cars:
        if player.distance(car) <= 20:
            game_is_on = False
            scoreboard.game_over()
            print("Game OVER!!")

    if player.ycor() >= 280:
        player.reset_player_position()
        scoreboard.increase_level()
        print("Next Level")

screen.exitonclick()