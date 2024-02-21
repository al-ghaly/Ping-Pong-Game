from turtle import Screen
from Paddle import Paddle
from Ball import Ball
from ScoreBoard import Board
import time

playing = True

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)
screen.listen()

right_paddle = Paddle()
right_paddle.goto(360, 0)
left_paddle = Paddle()
left_paddle.goto(-360, 0)

ball = Ball()

board = Board()

screen.onkeypress(fun=right_paddle.go_up, key="Up")
screen.onkeypress(fun=right_paddle.go_down, key="Down")

screen.onkeypress(fun=left_paddle.go_up, key="w")
screen.onkeypress(fun=left_paddle.go_down, key="s")

try:
	while playing:
	    time.sleep(ball.move_speed)
	    screen.update()
	    ball.move()

	    if ball.detect_wall():
	        ball.wall_bounce()

	    if (ball.distance(right_paddle) < 60 and ball.xcor() > 330) or (ball.distance(left_paddle) < 60 and ball.xcor() < -330):
	        ball.paddle_bounce()
	    elif ball.xcor() > 360:
	        board.update_left()
	        time.sleep(.5)
	        ball.reset_position()
	    elif ball.xcor() < -360:
	        board.update_right()
	        time.sleep(.5)
	        ball.reset_position()
except:
	pass


