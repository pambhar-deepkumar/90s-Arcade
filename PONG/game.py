from turtle import Screen
from pongball import Pongball
from paddle import Paddle
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("PONG")
screen.tracer(0)


lpaddle = Paddle(350, 0)
rpaddle = Paddle(-350, 0)

ball = Pongball()

screen.listen()
screen.onkey(lpaddle.move_up, "Up")
screen.onkey(lpaddle.move_down, "Down")
screen.onkey(rpaddle.move_up, "w")
screen.onkey(rpaddle.move_down, "s")

game_is_on = 1
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(0.1)
screen.exitonclick()
