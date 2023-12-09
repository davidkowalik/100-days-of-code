from turtle import Turtle, Screen
import random



is_race_on = True
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
y = [-125, -75, -25, 25, 75, 125]

for turtle_index in range(0, 6):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(colors[turtle_index])
    turtle.goto(x=-240, y=y[turtle_index])
    turtles.append(turtle)


user_bet = screen.textinput(title="Make Your bet", prompt="Witch turtle will win the race? Enter a color: ")

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
        if turtle.xcor() >= 210:
            is_race_on = False
            winner = turtle

if winner.pencolor() == user_bet:
    print("You won!!!")
else:
    print(f"You lost, {winner.pencolor()} won!")

screen.exitonclick()