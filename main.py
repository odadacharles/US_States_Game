import turtle
import pandas as pd
import csv

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

states_data = pd.read_csv('50_states.csv')
states_list = states_data['state'].to_list()
state_x = states_data['x'].to_list()
state_y = states_data['y'].to_list()

found_states = []


state_write = turtle.Turtle()
state_write.hideturtle()
state_write.penup()

while len(found_states) != 50:
    answer_state = screen.textinput(title=f"{len(found_states)}/50 States Correct",
                                    prompt="Enter another state name").title()
    if answer_state == "Exit":
        break
    if answer_state in states_list and answer_state not in found_states:
        index = states_list.index(answer_state)
        state_write.goto(int(state_x[index]), int(state_y[index]))
        state_write.write(f"{answer_state}", False, align="center", font=("Garamond", 10, 'bold'))
        found_states.append(answer_state)
missing_states = [state for state in states_list if state not in found_states]
missing_states_DF = pd.DataFrame(missing_states)
missing_states_DF.to_csv('missing_states.csv')

