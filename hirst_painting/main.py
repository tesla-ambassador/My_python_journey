# import colorgram
# color_palette = colorgram.extract('hirst_painting/hirst_image.jpg', 10)

# color_array = []
# for color in color_palette:
#     color_array.append((color.rgb.r, color.rgb.g, color.rgb.b))

import turtle as t
import random
    
color_list = [(233, 233, 232), (231, 233, 237), (236, 231, 233), (224, 233, 227), 
              (207, 160, 82), (54, 88, 130), (145, 91, 40), (140, 26, 49), (221, 207, 105), (132, 177, 203)]

tod = t.Turtle()
t.colormode(255)
tod.penup()
tod.hideturtle()
tod.sety(-200)
tod.speed('fastest')

def reset_pos():
    tod.left(90)
    tod.forward(50)
    tod.right(90)
    

def make_dots(no_steps):
    step = 1
    while step <= no_steps:
        tod.setx(-200)
        for i in range(no_steps):
            tod.dot(20)
            tod.color(random.choice(color_list))
            tod.forward(50)
        reset_pos()
        step += 1
        
make_dots(10)

screen = t.Screen()
screen.exitonclick()