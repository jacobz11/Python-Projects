import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
IMAGE = "blank_states_img.gif"
screen.addshape(IMAGE)
turtle.shape(IMAGE)

all_states = pandas.read_csv("50_states.csv")
list_states = all_states.state.to_list()
guessed_states = []
game_is_on = True
while game_is_on:
    user_answer = (screen.textinput(title=f"{len(guessed_states)}/50 states correct",
                                    prompt="What's another state's name").title())
    print(user_answer)
    state_row = all_states[all_states.state == user_answer]
    if user_answer in list_states:
        guessed_states.append(user_answer)
        state_print = turtle.Turtle()
        state_print.hideturtle()
        state_print.penup()
        state_print.goto(state_row['x'][state_row.index[0]], state_row['y'][state_row.index[0]])
        state_print.write(user_answer, align="center", font=("Courier", 7, "normal"))
        print(f"{state_row['x'][state_row.index[0]]} {state_row['y'][state_row.index[0]]}")
    if len(guessed_states) == 50 or user_answer == "Exit":
        game_is_on = False

missing_states = [state for state in list_states if state not in guessed_states]

data = pandas.DataFrame(missing_states)
data.to_csv("missing_states.csv")


