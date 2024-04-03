from paddle import Paddle
from turtle import Screen
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong Game")
screen.tracer(0)
ball = Ball()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")


is_game_running = True
while is_game_running:
    ball.move()
    screen.update()
    time.sleep(0.30)


screen.exitonclick()


