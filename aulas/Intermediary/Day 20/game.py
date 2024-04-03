from turtle import Turtle, Screen


screen = Screen()
screen.setup(500,600)
screen.bgcolor('black')
screen.title("Snake Game")


snake = Snake()
screen.exitonclick()

