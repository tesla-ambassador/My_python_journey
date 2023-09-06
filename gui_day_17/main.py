from turtle import Turtle, Screen
import random

gamabunta = Turtle()
gamabunta.shape('turtle')
gamabunta.color('cyan')

def change_color():
  R = random.random()
  G = random.random()
  B = random.random()
  
  gamabunta.color(R, G, B)  

# for i in range(10):
#     gamabunta.forward(10)
#     gamabunta.penup()
#     gamabunta.forward(10)
#     gamabunta.pendown()

sides = 3
while sides <= 10:
    side_angle = 360/sides
    change_color()
    for i in range(sides):
        gamabunta.forward(100)
        gamabunta.right(side_angle)
    sides += 1





mobyoku = Screen()
mobyoku.exitonclick()