from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make a bet', prompt='Choose a turtle (A name from the TMNT): ')

turtle_colors = ['red', 'blue', 'purple', 'gold']
turtles_array = []

for i in range(0, len(turtle_colors)):
    turtle = Turtle(shape='turtle')
    turtle.color(turtle_colors[i])
    turtle.penup()
    turtle.goto(-250, -50 + (i * 50))
    turtles_array.append(turtle)
    
if user_bet:
    is_race_on = True
          
while is_race_on:
    for turt in turtles_array:
        if turt.xcor() > 230:
            is_race_on = False
            winner = turt.pencolor()
            if winner == user_bet:
                print(f'You have won the bet, the winner was {winner}')
            else:
                print(f'You have lost the bet, the winner was {winner}')
        turt.forward(random.randint(0, 10))

screen.exitonclick()