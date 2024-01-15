from turtle import Screen
from paddle import Paddle
from line import Line
from scoreboard import ScoreBoard
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("my pong game")
screen.tracer(0)

line = Line()
score = ScoreBoard()
r_paddle = Paddle((380, 0))
l_paddle = Paddle((-390, 0))
ball = Ball()
screen.listen()
screen.onkeypress(fun=l_paddle.up, key="q")
screen.onkeypress(fun=l_paddle.down, key="a")
screen.onkeypress(fun=r_paddle.up, key="Up")
screen.onkeypress(fun=r_paddle.down, key="Down")

game_on = True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detecting collision wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 350 or ball.distance(l_paddle) < 50 and ball.xcor() < -360:
        ball.bounce_x()

    # Detect if the paddle misses the ball
    if ball.xcor() > 390:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -400:
        ball.reset_position()
        score.r_point()

screen.exitonclick()
