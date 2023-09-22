from turtle import Turtle, Screen
from state import State
import pandas as pd
import time

screen = Screen()
turtle = Turtle()
state = State()


image = 'usa_game/blank_states_img.gif'
screen.addshape(image)
screen.title('Can you name all 50 states?')
turtle.shape(image)

data = pd.read_csv('usa_game/50_states.csv')
df = pd.DataFrame(data)
state_list = list(df['state'])
score = 0
correct_guesses = []

while len(correct_guesses) < 50:
    time.sleep(0.1)
    answer_prompt = screen.textinput(title=f'Input State name: {score}/{len(state_list)} States Correct', prompt='Can you guess the State?').title()
    if answer_prompt == 'Exit':
        missing_states = [state for state in state_list if state not in correct_guesses]
        missing_states_df = pd.DataFrame(missing_states)
        missing_states_df.to_csv('./usa_game/missing_states.csv')
        break
    if answer_prompt in state_list and answer_prompt not in correct_guesses:
        correct_guesses.append(answer_prompt)
        score += 1
        matching_state = df[df['state'] == answer_prompt]
        state.write_and_move_state(answer_prompt, int(matching_state['x']), int(matching_state['y']))

screen.mainloop()