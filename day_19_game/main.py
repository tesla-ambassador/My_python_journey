from turtle import Turtle, Screen

tim = Turtle()
tim.speed(9)

def move_forwards():
    tim.forward(10)
    
def move_backwards():
    tim.back(10)
    
def counter_clockwise():
    tim.right(10)
    
def clockwise():
    tim.left(10)
    
def reset_turtle():
    screen.reset()

screen = Screen()
screen.listen()
screen.onkey(key='a', fun=clockwise)
screen.onkey(key='d', fun=counter_clockwise)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='c', fun=reset_turtle)
screen.exitonclick()