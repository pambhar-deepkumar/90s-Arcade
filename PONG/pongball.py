from turtle import Turtle


class Pongball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.penup()

    def move(self):
        self.goto(self.xcor() + 10, self.ycor() + 10)
