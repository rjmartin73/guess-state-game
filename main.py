import turtle as t
import pandas as pd
turtle = t.Turtle()
screen = t.Screen()
screen.setup(width=800, height=600)
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

state_data = pd.read_csv("50_states.csv")

# print(state_data)
state_names = state_data["state"].tolist()
# print(type(state_names))
total = 0
while total < 50:

    guess = screen.textinput("U.S. States Quiz", "Enter the name of a state?").title()
    if guess in state_names:
        lbl = t.Turtle()
        lbl.penup()
        lbl.hideturtle()
        x_pos = int(state_data.x[state_data.state == guess])
        y_pos = int(state_data.y[state_data.state == guess])
        position = (x_pos, y_pos)
        lbl.goto(position)
        lbl.write(guess, "left")
        state_names.remove(guess)
        total += 1
    print(f"{total}/50")
    # print(position)


screen.exitonclick()