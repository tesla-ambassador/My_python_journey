from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.write_scoreboard()
        
    def write_scoreboard(self):
        self.penup()
        self.speed('fastest')
        self.goto(0, 270)
        self.hideturtle()
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        
    def update_score(self):
        self.score += 1
        self.clear()
        self.write_scoreboard()
        
    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align=ALIGNMENT, font=FONT)