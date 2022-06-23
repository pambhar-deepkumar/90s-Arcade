import time
from turtle import Screen

from SNAKE.food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snakes")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.new_position()
        snake.add_one_unit()
        scoreboard.update_scoreboard()

    if snake.head.ycor() > 280 or snake.head.ycor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    for part_of_body in snake.square_body[1:]:
        if snake.head.distance(part_of_body) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
