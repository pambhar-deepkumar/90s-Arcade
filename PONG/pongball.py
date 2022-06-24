from turtle import Turtle


class Pongball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("cyan")
        self.penup()
        self.x_increment = 10
        self.y_increment = 10

    def move(self):
        self.goto(self.xcor() + self.x_increment, self.ycor() + self.y_increment)

    def bounce_x(self):
        self.x_increment *= -1

    def bounce_y(self):
        self.y_increment *= -1

    def ball_reset(self):
        self.goto(0, 0)
        self.bounce_x()
