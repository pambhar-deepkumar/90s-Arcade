from turtle import Screen
from turtle import Turtle

import playsnake
import ponggame


def switch():
    t.goto(-350, -t.ycor())


def initiate_game():
    if t.ycor() > 0:
        ponggame.start()
    else:
        playsnake.start()


if __name__ == '__main__':
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(height=500, width=800)
    screen.title("Menu")
    t = Turtle()
    t.speed("fastest")
    t.forward(10)
    t.penup()
    t.hideturtle()
    t.color("white")
    t.goto(0, 150)
    t.write("90's Arcade", align="center", font=("Courier", 50, "normal"))
    t.goto(0, 0)
    t.write("Multiplayer Pong", align="center", font=("Courier", 50, "normal"))
    t.goto(0, -70)
    t.write("Classic Snakes", align="center", font=("Courier", 50, "normal"))
    t.goto(-350, 35)
    t.showturtle()
    t.shape("circle")
    t.color("white")
    screen.listen()
    screen.onkeypress(switch, "Up")
    screen.onkeypress(switch, "Down")
    screen.onkeypress(initiate_game, 'space')
    screen.exitonclick()
