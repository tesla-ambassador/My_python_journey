from turtle import Screen
from player import Player
from ball import Ball
from scoreboard import Scoreboard
import time

is_game_on = True
sleep_time = 1
screen = Screen()
screen.setup(width=740, height=600)
screen.tracer(0)

player_one = Player()
player_two = Player()
ball = Ball()
score = Scoreboard()

player_one.paddle.goto(350, 0)
player_two.paddle.goto(-350, 0)

screen.listen()
screen.onkey(player_one.move_up, 'Up')
screen.onkey(player_one.move_down, 'Down')
screen.onkey(player_two.move_up, 'w')
screen.onkey(player_two.move_down, 's')

while is_game_on:
    time.sleep(sleep_time/10)
    screen.update()
    ball.move()
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    if ball.xcor() > 320:
        
        if ball.distance(player_one.paddle) < 50:
            ball.bounce_x()
            sleep_time -= 0.1
        
        elif ball.xcor() > 350:
            score.l_point() 
            ball.x_increment *= -1
            ball.home()
            sleep_time = 1
            
    elif ball.xcor() < -320:
        
        if ball.distance(player_two.paddle) < 50:
            ball.bounce_x()
            sleep_time += 0.1
            
        elif ball.xcor() < -350:
            score.r_point()
            ball.x_increment *= -1
            ball.home()
            sleep_time = 1
    
screen.exitonclick()