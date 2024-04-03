from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.coord_x = position[0]
        self.coord_y = position[1]
        self.shape(name="square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def move_up(self):
        self.coord_y += 25
        self.goto(self.coord_x, self.coord_y)

    def move_down(self):
        self.coord_y -= 25
        self.goto(self.coord_x, self.coord_y)
