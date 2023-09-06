import turtle as t
import random

# colors = ['CornFlowerBlue', 'DarkOrchid', 'IndianRed', 'DeepSkyBlue', 'LightSeaGreen', 'wheat', 'SlateGray', 'SeaGreen']
angles = [90, 180, 270, 0]

tim = t.Turtle()
tim.shape('turtle')
tim.pensize(10)
tim.speed(8)
t.colormode(255)

def change_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    return (r, g, b)

def random_walk():
    tim.color(change_color())
    tim.forward(20)
    tim.setheading(random.choice(angles))
    
for _ in range(200):
    random_walk()

screen = t.Screen()
screen.exitonclick()