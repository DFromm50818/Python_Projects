import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.bgpic("blank_states_img.gif")
state_list = pandas.read_csv("50_states.csv")
all_states = state_list["state"].tolist()
turtle.penup()
turtle.hideturtle()
guessed_states = []

def check_answer(answer, states):
    if answer in states["state"].values:
        all_states.remove(answer)
        return True
    else:
        return False

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/{len(state_list)} States Correct", prompt="What's another state name?")
    answer_state_uppercase = answer_state.title()
    guessed = check_answer(answer_state_uppercase, state_list)
    if answer_state_uppercase == "Exit":
        user_save = pandas.DataFrame({f"State": all_states})
        user_save.to_csv("missing_states.csv")
        break
    if guessed == True:
        result_df = state_list[state_list.state == answer_state_uppercase]
        result = result_df.values.tolist()[0]
        guessed_states.append(result)
        turtle.goto(result[1], result[2])
        turtle.write(result[0])



# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()