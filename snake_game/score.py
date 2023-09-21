from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('snake_game/data.txt') as h_score:
            self.high_score = int(h_score.read())
        self.penup()
        self.speed('fastest')
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('snake_game/data.txt', 'w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score()
        
    def increase_score(self):
        self.score += 1
        self.update_score()