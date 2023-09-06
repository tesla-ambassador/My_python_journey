from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-220, 250)
        self.level = 1
        self.update_scoreboard()
        
        
    def update_scoreboard(self):
        self.write(f"Level: {self.level}", align='center', font=FONT)
        
    def increment_level(self):
        self.clear()
        self.level += 1
        self.update_scoreboard()
        
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align='center', font=FONT)
