from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('gray')
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.penup()
        self.x_increment = 10
        self.y_increment = 10
        
    def move(self):
        new_x = self.xcor() + self.x_increment
        new_y = self.ycor() + self.y_increment
        self.goto(new_x, new_y)
        
    def bounce_y(self):
        self.y_increment *= -1
        
    def bounce_x(self):
        self.x_increment *= -1
        
    