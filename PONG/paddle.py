from turtle import Turtle


class Paddle:
    def __init__(self, x_cor, y_cor):
        pad = Turtle()
        pad.goto(x_cor, y_cor)
        pad.color("white")
        pad.shape("square")
        pad.shapesize(stretch_wid=5, stretch_len=1)
        pad.penup()
        self.paddle = pad

    def move_up(self):
        self.paddle.goto(self.paddle.xcor(), self.paddle.ycor() + 20)

    def move_down(self):
        self.paddle.goto(self.paddle.xcor(), self.paddle.ycor() - 20)
