import time
from turtle import Screen

from paddle import Paddle
from pongball import Pongball

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("PONG")
screen.tracer(0)

lpaddle = Paddle(-350, 0)
rpaddle = Paddle(350, 0)

ball = Pongball()

screen.listen()
screen.onkey(rpaddle.move_up, "Up")
screen.onkey(rpaddle.move_down, "Down")
screen.onkey(lpaddle.move_up, "w")
screen.onkey(lpaddle.move_down, "s")

game_is_on = 1
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(0.05)

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(rpaddle) < 50 and ball.xcor() > 320 or ball.distance(lpaddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.ball_reset()

    if ball.xcor() < -380:
        ball.ball_reset()

screen.exitonclick()
