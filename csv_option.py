import turtle
import csv

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

with open('50_states.csv') as states_file:
    states_data = csv.reader(states_file)
    states_list = []
    state_x = []
    state_y = []
    for row in states_data:
        state = row[0]
        x_coor = row[1]
        y_coor = row[2]
        states_list.append(state)
        state_x.append(x_coor)
        state_y.append(y_coor)

found_states = []
correct_count = 0

state_write = turtle.Turtle()
state_write.hideturtle()
state_write.penup()

while correct_count != 50:
    answer_state = screen.textinput(title=f"{correct_count}/50 States Correct", prompt="Enter another state name").title()
    if answer_state in states_list and answer_state not in found_states:
        index = states_list.index(answer_state)
        state_write.goto(int(state_x[index]), int(state_y[index]))
        state_write.write(f"{answer_state}", False, align="center", font=("Garamond", 10, 'bold'))
        correct_count += 1
        found_states.append(answer_state)

turtle.mainloop()
