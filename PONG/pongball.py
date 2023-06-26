from turtle import Turtle


class Pongball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("cyan")
        self.penup()
        self.x_increment = 10
        self.y_increment = 10
        self.ball_speed = 0.2

    def move(self):
        self.goto(self.xcor() + self.x_increment, self.ycor() + self.y_increment)

    def bounce_x(self):
        self.x_increment *= -1
        self.ball_speed *= 0.9
        
    def bounce_y(self):
        self.y_increment *= -1

    def ball_reset(self):
        self.ball_speed = 0.1
        self.goto(0, 0)
        self.bounce_x()

    def testing_sonar_qube(self):
        print("Print something!")
        pass
        

if __name__=="__main__":
    secret_key = "qkwjfch_123"
