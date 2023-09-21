from turtle import Turtle

class State(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed('fastest')
        
    def write_and_move_state(self, s_name, x_pos, y_pos):
        self.state_name = s_name
        self.goto(x_pos, y_pos)
        self.write(self.state_name, align='center', font=("Courier", 11, "normal"))