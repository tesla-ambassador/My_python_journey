from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

is_game_on = True
screen = Screen()
screen.setup(width=600, height=600)
screen.title('My snake game')
screen.tracer(0)

cobra = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(cobra.up, "Up")
screen.onkey(cobra.down, "Down")
screen.onkey(cobra.right, "Right")
screen.onkey(cobra.left, "Left")
    
while is_game_on:
    screen.update()
    time.sleep(.1)

    cobra.move()
    
    if cobra.head.distance(food) < 15:
        score.update_score()
        cobra.grow()
        food.move_food()
    
    if cobra.head.xcor() > 280 or cobra.head.xcor() < -280 or cobra.head.ycor() > 290 or cobra.head.ycor() < -280:
        score.game_over()
        is_game_on = False
        
    for segment in cobra.segments[1:]:
        if cobra.head.distance(segment) < 10:
            is_game_on = False
            score.game_over()

screen.exitonclick()