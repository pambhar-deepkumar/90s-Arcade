from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snakes")

sqaures = []

for a in range(0, 3):
    sqaures.append(Turtle())
    sqaures[a].shape("square")
    sqaures[a].penup()
    sqaures[a].goto(0 + a * -20, 0)
    sqaures[a].color("white")

screen.exitonclick()
