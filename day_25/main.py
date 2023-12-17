import turtle
import pandas as pd

def check_state(name, state_data):
    return states_data[states_data["state"] == name.title()]

def print_state(state_to):
    new_state.setposition(int(state_to.x), int(state_to.y))
    new_state.write(state_to["state"].item(), move=False, align="center", font=('Consolas', 10, 'normal'))


screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=800, height=600)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# turtle initialization - turtle will be writing states names on a map
new_state = turtle.Turtle()
new_state.hideturtle()
new_state.penup()
new_state.speed(0)



# CSV import 
states_data = pd.read_csv("50_states.csv")


correct_guesses = 0
game_on = True


while game_on:
    answer_state = screen.textinput(title=f"{correct_guesses}/50 States Correct ", prompt="What's another state's name?")
    if answer_state == "exit":
        game_on = False

    state_to_print = check_state(answer_state, states_data)
    if len(state_to_print) > 0:
        print_state(state_to_print)
        correct_guesses += 1




