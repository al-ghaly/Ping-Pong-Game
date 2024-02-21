from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_step = 12
        self.y_step = 9
        self.move_speed = .1

    def move(self):
        self.goto(self.xcor() + self.x_step, self.ycor() + self.y_step)

    def wall_bounce(self):
        self.y_step *= -1

    def detect_wall(self):
        return self.ycor() > 280 or self.ycor() < -280

    def paddle_bounce(self):
        self.x_step *= -1
        self.move_speed *= .9

    def reset_position(self):
        self.move_speed = .1
        self.goto(0, 0)
        self.paddle_bounce()
