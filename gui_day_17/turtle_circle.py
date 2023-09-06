import turtle as t
import random

tom = t.Turtle()
tom.color('SlateGray')
tom.speed('fastest')
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    return (r, g, b)


def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        tom.color(random_color())
        tom.circle(100, 360)
        tom.setheading(i*size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()