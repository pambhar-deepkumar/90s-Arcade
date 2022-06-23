from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.square_body = []
        for pos in STARTING_POSITION:
            new_square = Turtle()
            new_square.shape("square")
            new_square.penup()
            new_square.goto(pos)
            new_square.color("white")
            self.square_body.append(new_square)
        self.head = self.square_body[0]

    def move(self):
        """Moves all the body blocks in the direction of the first"""
        for j in range(len(self.square_body) - 1, 0, -1):
            self.square_body[j].goto(self.square_body[j - 1].xcor(), self.square_body[j - 1].ycor())
        self.square_body[0].forward(MOVE_DISTANCE)

    def up(self):
        if not self.square_body[0].heading() == 270:
            self.square_body[0].setheading(90)

    def down(self):
        if not self.square_body[0].heading() == 90:
            self.square_body[0].setheading(270)

    def right(self):
        if not self.square_body[0].heading() == 180:
            self.square_body[0].setheading(0)

    def left(self):
        if not self.square_body[0].heading() == 0:
            self.square_body[0].setheading(180)

    def add_one_unit(self):
        new_square = Turtle()
        new_square.shape("square")
        new_square.penup()
        new_square.color("white")
        self.square_body.append(new_square)
        self.move()