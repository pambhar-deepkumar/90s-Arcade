from turtle import Turtle
ALIGNMENT ="center"
FONT = ("Verdana",15, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.count =0
        self.color("white")
        self.penup()
        self.ht()
        self.goto(0,275)
        self.write(f"Score = {self.count}",font=FONT, align=ALIGNMENT)

    def update_scoreboard(self):
        self.count+=1
        self.clear()
        self.write(f"Score = {self.count}",font=FONT, align=ALIGNMENT)