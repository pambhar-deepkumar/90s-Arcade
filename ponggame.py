import time
from turtle import Screen

from PONG.paddle import Paddle
from PONG.pongball import Pongball
from PONG.scoreboard import Scoreboard


def start():
    screen = Screen()
    screen.clear()
    screen.bgcolor("black")
    screen.setup(height=600, width=800)
    screen.title("PONG")
    screen.tracer(0)

    scoreboard = Scoreboard()
    l_paddle = Paddle(-350, 0)
    r_paddle = Paddle(350, 0)

    ball = Pongball()

    screen.listen()
    screen.onkeypress(r_paddle.move_up, "Up")
    screen.onkeypress(r_paddle.move_down, "Down")
    screen.onkeypress(l_paddle.move_up, "w")
    screen.onkeypress(l_paddle.move_down, "s")

    game_is_on = 1
    while game_is_on:
        screen.update()
        ball.move()
        time.sleep(ball.ball_speed)

        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
            ball.bounce_x()

        if ball.xcor() > 380:
            ball.ball_reset()
            scoreboard.l_update()

        if ball.xcor() < -380:
            ball.ball_reset()
            scoreboard.r_update()

    screen.exitonclick()
