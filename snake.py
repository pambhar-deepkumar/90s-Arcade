from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.sqaures = []
        for pos in STARTING_POSITION:
            new_square = Turtle()
            new_square.shape("square")
            new_square.penup()
            new_square.goto(pos)
            new_square.color("white")
            self.sqaures.append(new_square)

    def move(self):
        for j in range(len(self.sqaures) - 1, 0, -1):
            self.sqaures[j].goto(self.sqaures[j - 1].xcor(), self.sqaures[j - 1].ycor())
        self.sqaures[0].forward(MOVE_DISTANCE)

    def up(self):
        self.sqaures[0].setheading(90)

    def down(self):
        self.sqaures[0].setheading(270)

    def right(self):
        self.sqaures[0].setheading(0)

    def left(self):
        self.sqaures[0].setheading(180)


