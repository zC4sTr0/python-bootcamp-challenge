from turtle import Turtle


class Snake:

    def __init__(self):
        self.size = 3
        self.position = 0
        self.turtle_square_1 = Turtle("square")
        self.turtle_square_2 = Turtle("square")
        self.turtle_square_3 = Turtle("square")
        self.turtle_square_1.color("white")
        self.turtle_square_2.goto(self.position-20, 0)
        self.turtle_square_2.color("white")
        self.turtle_square_3.goto(self.position-40, 0)
        self.turtle_square_3.color("white")

    def move_forward(self):
        self.position += 20

    def print(self):
        return [self.position, self.position+20, self.position+40]
